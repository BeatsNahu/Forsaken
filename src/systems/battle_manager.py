import pygame
import random
import config
from core.scene import Scene
from systems.ui_components import BattleHUD
from systems.dialogue_player import DialoguePlayer
from overlays.inventory_menu import InventoryMenu
class BattleManager(Scene):
    def __init__(self, engine, data=None):
        super().__init__(engine, data) # Get base initialization (Scene, Data, etc.)

        self.ui = BattleHUD(self.engine) # UI for battle
        self._dialogue_player = None # Dialogue player for managing dialogue

        # State variables of the battle
        self.ui_state = "PRE_BATTLE"  # CHOOSE_ACTION, CHOOSE_TARGET, CHOOSE_ITEM
        self.player_selection = 0        # Index of selected player action
        self.target_selection = 0
        self.player_is_defending = False
        self.turn = 0                    # 0=player, 1=enemy
        
        # Battle data
        self.player_skills = [] # List of player skills (from data)
        self.enemies = []       # List of enemy dicts (from data)
        self.life_player = 50

        # Visual elements
        self.static_layers = [] # For (base, light, floor)
        
        # Temp variables for enemy turn timing
        self._enemy_turn_timer = 0.0
        self._enemy_action_pending = False
        self._enemy_anim_timer = 0.0

        # Dialogue UI
        self._pending_target_scene = None

        # Attack effects
        self.damage_flash_timer = 0.0
        self.damage_flash_duration = 0.3
        self.flash_veil = pygame.Surface(self.engine.screen.get_size(), pygame.SRCALPHA)

        # Log battle outcome
        self.battle_log_text = ""
        self.battle_log_timer = 0.0
        self.log_font = self.engine.load_font(None, 24)

    def enter(self):
        # Inicializa bonus de daño del jugador si no existe
        if "player_base_damage" not in self.engine.state:
            self.engine.state["player_base_damage"] = 0
        
        # Load static layers
        self.static_layers = [] # (base, light, floor) 
        screen_size = self.engine.screen.get_size() 

        for layer_data in self.data.get("static_layers", []):
            surf = self.engine.load_image(layer_data.get("image"))
            if not surf:
                print(f"Advertencia: No se pudo cargar la capa {layer_data.get('image')}")
                continue
            
            # Scale if needed
            if layer_data.get("scale_to_screen", False):
                surf = pygame.transform.scale(surf, screen_size)

            pos = layer_data.get("pos", [0, 0])
            self.static_layers.append( (surf, pos) ) # Store tuple (surface, position)

        # Load player data 
        self.life_player = self.engine.state.get("player_hp", 50)
        self.player_skills = self.data.get("player", {}).get("skills", [])

        # Load music
        music_path = self.data.get("music")
        if music_path:
            self.engine.play_music(music_path, loop=-1)

        # Load dialogue
        pre_dialogue = self.data.get("pre_battle_dialogue")

        if pre_dialogue:
            self.ui_state = "PRE_BATTLE"
            self._dialogue_player = DialoguePlayer(self.engine, pre_dialogue)
        else:
            # If there's no dialogue, jump straight into the battle
            self.ui_state = "BATTLE"
            self._return_to_player_turn()   
        
        # Load enemies
        self.enemies = []
        for enemy_data in self.data.get("enemies", []):
            # Load and scale enemy sprite
            sprite_surf = self.engine.load_image(enemy_data.get("sprite"))
            scale_factor_s = enemy_data.get("sprite_scale_factor", 1.0) # Default 1 (no scale)
            if sprite_surf and scale_factor_s != 1.0:
                new_size = (int(sprite_surf.get_width() * scale_factor_s), 
                            int(sprite_surf.get_height() * scale_factor_s))
                sprite_surf = pygame.transform.scale(sprite_surf, new_size)

            # Load and scale HP bar
            hp_bar_surf = self.engine.load_image(enemy_data.get("hp_bar_sprite"))
            scale_factor_hp = enemy_data.get("hp_bar_scale_factor", 1.0)
            if hp_bar_surf and scale_factor_hp != 1.0:
                new_size = (int(hp_bar_surf.get_width() * scale_factor_hp), 
                            int(hp_bar_surf.get_height() * scale_factor_hp))
                hp_bar_surf = pygame.transform.scale(hp_bar_surf, new_size)

            enemy = {
                "id": enemy_data.get("id"),
                "type": enemy_data.get("type"),
                "hp": enemy_data.get("hp", 10),
                "max_hp": enemy_data.get("max_hp", 10),
                "skills": enemy_data.get("skills", []),
                "pos": enemy_data.get("pos", [1500, 300]),
                
                # Store the loaded and scaled surfaces
                "sprite": sprite_surf,
                "hp_bar_sprite": hp_bar_surf,
                "hp_bar_pos": enemy_data.get("hp_bar_pos", [1500, 250]),
                "hp_bar_pos": enemy_data.get("hp_bar_pos", [1500, 250]),
                "hp_bar_scale": scale_factor_hp
            }
            self.enemies.append(enemy)
        
        self.rules = self.data.get("rules", {})
        if self.rules.get("turn_order") == "player_first":
            self.turn = 0
        else:
            self.turn = 1

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
            
        # Block input if it's not the player's turn
        if self.turn != 0:
            return
        
        # If a dialogue player exists, it handles the event.
        if self._dialogue_player:
            self._dialogue_player.handle_event(event)
        
        # Otherwise the battle handles the event
        elif self.ui_state == "CHOOSE_ACTION":
            if event.key == pygame.K_DOWN:
                self.player_selection = (self.player_selection + 1) % len(self.player_skills)
            elif event.key == pygame.K_UP:
                self.player_selection = (self.player_selection - 1) % len(self.player_skills)
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self._select_action()

    def _select_action(self):
        skill = self.player_skills[self.player_selection]
        
        if skill["type"] == "ATTACK":
            self.target_selection = 0 
            self._confirm_target()

        elif skill["type"] == "DEFEND":
            self.player_is_defending = True
            self._end_player_turn()

        elif skill["type"] == "ITEM_MENU":
            self.engine.push_overlay(InventoryMenu(self.engine))

    def _confirm_target(self):
        # The player has chosen Enter
        skill = self.player_skills[self.player_selection]
        target = self.enemies[self.target_selection]
        
        # 1. Apply skill logic
        if skill["type"] == "ATTACK":
            base_dmg = skill.get("dmg", 0)
            bonus_dmg = self.engine.state.get("player_base_damage", 0)
            total_dmg = base_dmg + bonus_dmg
            print(f"DEBUG: Base damage={base_dmg}, bonus={bonus_dmg}, total={total_dmg}")
            cost = skill.get("cost", 0)
            
            target["hp"] -= total_dmg
            self.life_player -= cost

            sfx_path = skill.get("sfx")
            if sfx_path:
                self.engine.play_sound(sfx_path)

            vfx_path = skill.get("vfx")
            if vfx_path:
                vfx_image = self.engine.load_image(vfx_path)
                if vfx_image:
                    center_pos = [960, 540]

                    self.engine.animation_manager.start_animation(
                        surface=vfx_image,
                        start_pos=center_pos,
                        end_pos=center_pos,
                        duration=0.2,
                        start_scale=1.0,
                        end_scale=5.0,
                        persist=False
                    )
                    
            self.battle_log_text = f"¡Golpeas a {target['id']} por {total_dmg} daño!"

        # 2. Check if the target died
        if target["hp"] <= 0:
            self.battle_log_text = f"{target['id']} has been defeated."
            self.enemies.pop(self.target_selection) # Remove from the alive list

        # 3. Check if the battle ended
        if not self.enemies:
            self._on_victory()
            return

        # 4. End the player's turn
        self._end_player_turn()

    def _end_player_turn(self):
        self.turn = 1
        self._enemy_action_pending = True
        self._enemy_turn_timer = 0.5 # 500ms delay
        self.ui_state = "ENEMY_TURN"

    def _execute_enemy_turn(self):
        print("--- Enemy Turn ---")
        self._enemy_action_pending = False # Prevent it from running again

        for enemy in self.enemies:
            if not enemy["skills"]:
                continue

            skill = enemy["skills"][0] # Simple AI

            if skill["type"] == "ATTACK":
                dmg = random.randint(skill.get("dmg_min", 2), skill.get("dmg_max", 6))

                if self.player_is_defending:
                    dmg = dmg // 2 

                self.life_player -= dmg
                print(f"{enemy['id']} used {skill['text']} for {dmg} damage.")

                self.damage_flash_timer = self.damage_flash_duration

                # 1. Show a notification (use your engine system)
                self.battle_log_text = f"{enemy['id']} attacks you for {dmg} damage."
                self.battle_log_timer = 2.0

                # 2. Play the enemy SFX (if any)
                sfx_path = skill.get("sfx")
                if sfx_path:
                    self.engine.play_sound(sfx_path)

                # 3. Start the enemy VFX (if any)
                vfx_path = skill.get("vfx")
                if vfx_path:
                    vfx_image = self.engine.load_image(vfx_path)
                    if vfx_image:
                        self.engine.animation_manager.start_animation(
                            surface=vfx_image,
                            start_pos=[960, 540],
                            end_pos=[960, 540],     
                            duration=0.5,
                            start_scale=1.0,
                            end_scale=5.0,
                            persist=False
                        )
                # 4. Start the 'cooldown' timer
                self._enemy_anim_timer = 1.0

        if self._enemy_anim_timer == 0.0:
            self._return_to_player_turn()

    def _return_to_player_turn(self):
        # 1. Check player defeat
        if self.life_player <= 0:
            self._on_defeat()
            return

        # 2. Return to player's turn
        self.turn = 0
        self.ui_state = "CHOOSE_ACTION"
        self.player_selection = 0
        self.player_is_defending = False

    def _on_victory(self):
        print("VICTORY!")
        # Apply rewards (unchanged)
        rewards = self.data.get("rewards_on_victory", {})
        self.engine.apply_effects(rewards.get("effects", []))

        # Store the target scene
        self._pending_target_scene = self.data.get("on_victory_target")
        post_dialogue = self.data.get("post_battle_dialogue")

        if post_dialogue:
            self.ui_state = "POST_BATTLE_VICTORY"
            self._dialogue_player = DialoguePlayer(self.engine, post_dialogue)
        else:
            if self._pending_target_scene:
                self.engine.scene_manager.load_scene(self._pending_target_scene)

    def _on_defeat(self):
        print("DEFEAT...")
        self._pending_target_scene = self.data.get("on_defeat_target")

        post_dialogue = self.data.get("post_defeat_dialogue") 

        if post_dialogue:
            self.ui_state = "POST_BATTLE_DEFEAT"
            self._dialogue_player = DialoguePlayer(self.engine, post_dialogue)
        else:
            if self._pending_target_scene:
                self.engine.scene_manager.load_scene(self._pending_target_scene)

    def update(self, dt: float): 
        # If a dialogue is playing, update it.
        if self._dialogue_player:
            self._dialogue_player.update(dt)
            
            # Check if it has finished
            if self._dialogue_player.is_finished():
                current_state = self.ui_state
                self._dialogue_player = None # Destroy it

                # Decide what to do next
                if current_state == "PRE_BATTLE":
                    self.ui_state = "BATTLE"
                    self._return_to_player_turn()
                
                elif current_state == "POST_BATTLE_VICTORY" or current_state == "POST_BATTLE_DEFEAT":
                    if self._pending_target_scene:
                        self.engine.scene_manager.load_scene(self._pending_target_scene)
            
        # If no dialogue, update battle logic
        elif self.ui_state in ("CHOOSE_ACTION", "ENEMY_TURN", "CHOOSE_TARGET"):
            if self._enemy_action_pending:
                self._enemy_turn_timer -= dt
                if self._enemy_turn_timer <= 0:
                    self._execute_enemy_turn()

            if self._enemy_anim_timer > 0:
                self._enemy_anim_timer -= dt
                if self._enemy_anim_timer <= 0:
                    self._return_to_player_turn()

        # 1. Update damage flash
        if self.damage_flash_timer > 0:
            self.damage_flash_timer -= dt

        # 2. Update battle log
        if self.battle_log_timer > 0:
            self.battle_log_timer -= dt
        else:
            self.battle_log_text = ""

    def draw(self, surface):
        surface.fill((0, 0, 0)) # Clear screen
        
        # 1. Stage Layers (base, light, floor)
        for surf, pos in self.static_layers:
            surface.blit(surf, pos)
            
        # 2. Layer of "Actors" (Enemies and their UI)
        for enemy in self.enemies:
            if enemy["sprite"]:
                surface.blit(enemy["sprite"], enemy["pos"])
            
            # Draw the HP bar
            if enemy["hp_bar_sprite"]:
                # 1. Draw the base of the bar
                surface.blit(enemy["hp_bar_sprite"], enemy["hp_bar_pos"])
                try:
                    # 2. Calculate HP percentage
                    hp_percent = max(0, enemy["hp"] / enemy["max_hp"])

                    # 3. Get scale and positions
                    scale = enemy.get("hp_bar_scale", 1.0) # Use the stored value
                    base_x = enemy["hp_bar_pos"][0]
                    base_y = enemy["hp_bar_pos"][1]

                    # 4. Calculate offsets (from config) scaled
                    offset_x = config.ENEMY_HP_BAR_OFFSET_X * scale
                    offset_y = config.ENEMY_HP_BAR_OFFSET_Y * scale
                    max_width = config.ENEMY_HP_BAR_WIDTH * scale
                    height = config.ENEMY_HP_BAR_HEIGHT * scale

                    # 5. Compute current width of the red bar
                    current_width = int(max_width * hp_percent)

                    # 6. Define the Rect for the red bar
                    bar_rect = pygame.Rect(
                        base_x + offset_x,  # X position of the bar
                        base_y + offset_y,  # Y position of the bar
                        current_width,      # Width (based on HP)
                        height              # Height
                    )

                    # 7. Draw the red rectangle
                    pygame.draw.rect(surface, config.COLOR_RED, bar_rect)

                except Exception as e:
                    print(f"Error drawing HP bar: {e}")

        if self.ui_state in ("PRE_BATTLE", "POST_BATTLE_VICTORY", "POST_BATTLE_DEFEAT"):
            if self._dialogue_player:
                self._dialogue_player.draw(surface)
            
        # 3: We're in Battle
        elif self.ui_state in ("CHOOSE_ACTION", "ENEMY_TURN", "CHOOSE_TARGET", "CHOOSE_ITEM"):
            # Draw the stats and skills panel
            self.ui.draw(
                surface,
                player_hp=self.life_player,
                enemies=self.enemies,
                skills=self.player_skills,
                selected_skill_idx=self.player_selection
            )

        # 4. Damage flash effect
        if self.damage_flash_timer > 0:
            # Calculate opacity (alpha). Fades from 150 to 0.
            progress = self.damage_flash_timer / self.damage_flash_duration
            alpha = int(progress * 150) # 150 is the max alpha (0-255)

            self.flash_veil.fill((255, 0, 0, max(0, alpha))) # Fill with translucent red
            surface.blit(self.flash_veil, (0, 0))

        # 5. Battle Log
        if self.battle_log_timer > 0 and self.battle_log_text:
            padding = 10

            # Render text
            text_surf = self.log_font.render(self.battle_log_text, True, (255, 255, 255))

            # Compute background size
            bg_width = text_surf.get_width() + padding * 2
            bg_height = text_surf.get_height() + padding * 2

            # Position (Top Right)
            screen_w = self.engine.screen.get_width()
            pos_x = screen_w - bg_width - 20 # 20px de margen
            pos_y = 20

            # Draw translucent background
            bg_surf = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
            bg_surf.fill((0, 0, 0, 150)) # Black, alpha 150
            surface.blit(bg_surf, (pos_x, pos_y))

            # Draw text on top of the background
            surface.blit(text_surf, (pos_x + padding, pos_y + padding))

SCENE_CLASS = BattleManager