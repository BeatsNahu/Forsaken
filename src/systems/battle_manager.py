import pygame
import random
from core.scene import Scene
from systems.ui_manager import BattleHUD

class BattleManager(Scene):
    def __init__(self, engine, data=None):
        super().__init__(engine, data) # Get base initialization (Scene, Data, etc.)

        self.ui = BattleHUD(self.engine) # UI for battle
        
        # State variables of the battle
        self.ui_state = "CHOOSE_ACTION"  # CHOOSE_ACTION, CHOOSE_TARGET, CHOOSE_ITEM
        self.player_selection = 0        # Index of selected player action
        self.target_selection = 0
        self.player_is_defending = False
        self.turn = 0                    # 0=player, 1=enemy
        
        # Battle data
        self.player_skills = [] # List of player skills (from data)
        self.enemies = []       # List of enemy dicts (from data)
        self.life_player = 10

        # Visual elements
        self.static_layers = [] # For (base, light, floor)
        
        # Temp variables for enemy turn timing
        self._enemy_turn_timer = 0.0
        self._enemy_action_pending = False

    def enter(self):
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
        self.life_player = self.engine.state.get("player_hp", 10)
        self.player_skills = self.data.get("player", {}).get("skills", [])

        # Load music
        music_path = self.data.get("music")
        if music_path:
            self.engine.play_music(music_path, loop=-1)
        
        # Load enemies
        self.enemies = []
        for enemy_data in self.data.get("enemies", []):
            
            # Cargar y escalar Sprite de Enemigo
            sprite_surf = self.engine.load_image(enemy_data.get("sprite"))
            scale_factor_s = enemy_data.get("sprite_scale_factor", 1.0) # Default 1 (sin escala)
            if sprite_surf and scale_factor_s != 1.0:
                new_size = (int(sprite_surf.get_width() * scale_factor_s), 
                            int(sprite_surf.get_height() * scale_factor_s))
                sprite_surf = pygame.transform.scale(sprite_surf, new_size)

            # Cargar y escalar Barra de HP
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
                "hp_bar_pos": enemy_data.get("hp_bar_pos", [1500, 250])
            }
            self.enemies.append(enemy)
        
        # Starting turn
        self.rules = self.data.get("rules", {})
        if self.rules.get("turn_order") == "player_first":
            self.turn = 0
        else:
            self.turn = 1
            
        self.ui_state = "CHOOSE_ACTION"
        self.player_selection = 0
        self.target_selection = 0

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_ESCAPE:
            setattr(self.engine, "quit_flag", True)
            
        # Block input if it's not the player's turn
        if self.turn != 0:
            return
        
        if self.ui_state == "CHOOSE_ACTION":
            # Navegar por el menú de habilidades
            if event.key == pygame.K_DOWN:
                self.player_selection = (self.player_selection + 1) % len(self.player_skills)
            elif event.key == pygame.K_UP:
                self.player_selection = (self.player_selection - 1) % len(self.player_skills)
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self._select_action()

    def _select_action(self):
        """The player has selected an action from the menu."""
        skill = self.player_skills[self.player_selection]
        
        if skill["type"] == "ATTACK":
            self.target_selection = 0 
            self._confirm_target()

        elif skill["type"] == "DEFEND":
            self.player_is_defending = True
            self._end_player_turn()

        elif skill["type"] == "ITEM_MENU":
            print("UI: Abriendo menú de items (no implementado)")
            # self.ui_state = "CHOOSE_ITEM"

    def _confirm_target(self):
        # The player has chosen Enter
        skill = self.player_skills[self.player_selection]
        target = self.enemies[self.target_selection]
        
        # 1. Aplicar lógica de la habilidad
        if skill["type"] == "ATTACK":
            dmg = skill.get("dmg", 0)
            cost = skill.get("cost", 0)
            
            target["hp"] -= dmg
            self.life_player -= cost

            sfx_path = skill.get("sfx")
            if sfx_path:
                self.engine.play_sound(sfx_path)

            vfx_path = skill.get("vfx")
            if vfx_path:
                vfx_image = self.engine.load_image(vfx_path)
                if vfx_image:
                    self.engine.animation_manager.start_animation(
                        surface=vfx_image,
                        id="vfx_hit",
                        start_pos=target["pos"],
                        end_pos=target["pos"],
                        duration=0.2,
                        start_scale=0.5,
                        end_scale=1.5,
                        persist=False
                    )
                    
            print(f"Jugador usó {skill['text']} en {target['id']} por {dmg} daño.")

        # 2. Comprobar si el objetivo murió
        if target["hp"] <= 0:
            print(f"{target['id']} ha sido derrotado.")
            self.enemies.pop(self.target_selection) # Eliminar de la lista de vivos

        # 3. Comprobar si la batalla terminó
        if not self.enemies:
            self._on_victory()
            return
            
        # 4. Terminar el turno
        self._end_player_turn()

    def _end_player_turn(self):
        self.turn = 1
        self._enemy_action_pending = True
        self._enemy_turn_timer = 0.5 # 500ms de retraso
        self.ui_state = "ENEMY_TURN"

    def _execute_enemy_turn(self):
        print("--- Turno Enemigo ---")
        for enemy in self.enemies:
            # Lógica de IA simple: usar la primera habilidad
            if not enemy["skills"]:
                continue
            
            skill = enemy["skills"][0]
            
            if skill["type"] == "ATTACK":
                dmg = random.randint(skill.get("dmg_min", 1), skill.get("dmg_max", 1))
                
                # Aplicar defensa del jugador
                if self.player_is_defending:
                    dmg = dmg // 2 # 50% de daño
                    
                self.life_player -= dmg
                print(f"{enemy['id']} usó {skill['text']} por {dmg} daño.")

        # 2. Comprobar derrota del jugador
        if self.life_player <= 0:
            self._on_defeat()
            return
            
        # 3. Volver al turno del jugador
        self.turn = 0
        self.ui_state = "CHOOSE_ACTION"
        self.player_selection = 0
        self.player_is_defending = False # Resetear defensa
        self._enemy_action_pending = False

    def _on_victory(self):
        print("¡VICTORIA!")
        # Aplicar recompensas
        rewards = self.data.get("rewards_on_victory", {})
        self.engine.apply_effects(rewards.get("effects", []))
        
        # Ir a la siguiente escena
        target = self.data.get("on_victory_target")
        if target:
            self.engine.scene_manager.load_scene(target)
            
    def _on_defeat(self):
        print("DERROTA...")
        # (Lógica de perder corazón, si la tuvieras)
        # self.engine.lose_heart()
        
        target = self.data.get("on_defeat_target")
        if target:
            self.engine.scene_manager.load_scene(target)

    def update(self, dt: float):
        # Update enemy turn timer
        if self._enemy_action_pending:
            self._enemy_turn_timer -= dt
            if self._enemy_turn_timer <= 0:
                self._execute_enemy_turn()

    def draw(self, surface):
        # 1. Stage Layers (base, light, floor)
        for surf, pos in self.static_layers:
            surface.blit(surf, pos)
            
        # 2. Layer of "Actors" (Enemies and their UI)
        for enemy in self.enemies:
            if enemy["sprite"]:
                surface.blit(enemy["sprite"], enemy["pos"])
            
            # Draw the HP bar
            if enemy["hp_bar_sprite"]:
                surface.blit(enemy["hp_bar_sprite"], enemy["hp_bar_pos"])
                # (Here's how to draw the red HP bar:
                # based on enemy["hp"] / enemy["max_hp"])

        # 3. Fixed UI Layer (Stats Panel, Skills Text, Player HP)
        self.ui.draw(
            surface,
            player_hp=self.life_player,
            enemies=self.enemies,
            skills=self.player_skills,
            selected_skill_idx=self.player_selection
        )
        
SCENE_CLASS = BattleManager