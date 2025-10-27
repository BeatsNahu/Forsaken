import pygame
import os
import random
from scene import Scene


class BattleManager(Scene):
    def __init__(self, engine, data=None):
        super().__init__(engine, data or {"id": "battle_manager"})

        self.ui_state = "CHOOSE_ACTION"  # "CHOOSE_ACTION", "CHOOSE_TARGET", "CHOOSE_ITEM"
        self.player_skills = [
            {"text": "Puño", "type": "ATTACK", "dmg": 5, "cost": 1},
            {"text": "Patada", "type": "ATTACK", "dmg": 2, "cost": 0},
            {"text": "Defensa", "type": "DEFEND"},
            {"text": "Item", "type": "ITEM_MENU"},
            ]
        self.enemies = [] # Lista de enemigos vivos (diccionarios)
        self.player_selection = 0
        self.target_selection = 0
        self.player_is_defending = False

        # Monster timing (so monster action is delayed slightly)
        self._monster_delay = 0.0
        self._monster_action_pending = False

        # fonts / visuals
        font_path = os.path.join("assets", "fonts", "press-start.k.ttf")
        self._font_path = font_path
        try:
            self.font = self.engine.load_font(self._font_path, 28)
        except Exception:
            self.font = pygame.font.Font(self._font_path if os.path.exists(self._font_path) else None, 28)

        self.bg = None
        self.title = "Battle"

    def enter(self):
    # 1. LLAMAR AL PADRE para cargar fuentes (¡Importante!)
        super().enter() 

    # 2. Usar el CACHÉ del motor
        bg_path = self.data.get("background", "assets/backgrounds/battle_scene.png")
        try:
            surf = self.engine.load_image(bg_path)
            if surf:
                self.bg = pygame.transform.scale(surf, self.engine.screen.get_size())
        except Exception as e:
            print(f"Error al cargar fondo de batalla: {e}")
            self.bg = None

    # 3. LEER los datos de la batalla (de ex_pelea.py)
        self.enemies_data = self.data.get("enemies", [])
        self.rules = self.data.get("rules", {})
        self.rewards = self.data.get("rewards", {})
    
    # 4. Crear los enemigos "vivos"
        self.enemies = []
        for enemy_def in self.enemies_data:
            self.enemies.append({
                "id": enemy_def.get("id"),
                "type": enemy_def.get("type"),
                "hp": enemy_def.get("hp", 10),
                "max_hp": enemy_def.get("hp", 10),
                "attack_min": enemy_def.get("attack_min", 1),
                "attack_max": enemy_def.get("attack_max", 3)
            })
    
    # 5. Cargar estado del jugador desde el ENGINE
        self.life_player = self.engine.state.get("player_max_hp", 10) # Asumiendo 10 como default
        self.player_hearts = self.engine.get_hearts()
    
    # ... (Decidir turno inicial basado en self.rules)
        self.turn = 0 # 0: player

    def start_battle(self, monster_type):
        # configure monster stats by type
        self.monster_type = monster_type
        if monster_type == "rat":
            self.life_monster = 10
            self.attack_damage = (1, 3)
        elif monster_type == "frog":
            self.life_monster = 11
            self.attack_damage = (1, 3)
        elif monster_type == "knife_guy":
            self.life_monster = 12
            self.attack_damage = (1, 4)
        else:
            # fallback generic
            self.life_monster = 8
            self.attack_damage = (1, 2)

        # decide who starts
        self.turn = random.randint(0, 1)
        self._monster_delay = 0.0
        self._monster_action_pending = False

    def _player_attack(self, choice_idx: int):
        # Player performs chosen attack
        if choice_idx == 0:
            # strong punch
            self.life_monster -= self.punch
            self.life_player -= 1
        else:
            # weak kick
            self.life_monster -= self.kick
            self.life_player = min(999, self.life_player + 1)

        # clamp
        if self.life_monster <= 0:
            # victory
            vscene = self.data.get("victory")
            if vscene:
                self.engine.scene_manager.load_scene(vscene)
            return

        # switch to monster turn and schedule action after small delay
        self.turn = 1
        self._monster_delay = 0.0
        self._monster_action_pending = True

    def _monster_attack(self):
        # Monster attacks: choose damage from the configured tuple
        dmg = random.randint(self.attack_damage[0], self.attack_damage[1])
        self.life_player -= dmg
        # check defeat
        if self.life_player <= 0:
            dscene = self.data.get("defeat")
            if dscene:
                self.engine.scene_manager.load_scene(dscene)
            return

        # back to player
        self.turn = 0
        self._monster_action_pending = False

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        # navigate options only on player's turn
        if self.turn == 0:
            if event.key == pygame.K_DOWN:
                self.player_selection = (self.player_selection + 1) % len(self.options)
                return
            if event.key == pygame.K_UP:
                self.player_selection = (self.player_selection - 1) % len(self.options)
                return

            # choose with 1/2 or Enter
            if event.key in (pygame.K_1, pygame.K_KP1):
                self._player_attack(0)
            elif event.key in (pygame.K_2, pygame.K_KP2):
                self._player_attack(1)
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self._player_attack(self.player_selection)

    def update(self, dt: float):
        # if monster action is pending, accumulate time then execute
        if self.turn == 1 and self._monster_action_pending:
            self._monster_delay += dt
            if self._monster_delay >= 0.6:  # 600ms delay
                self._monster_attack()

    def draw(self, surface):
        # background
        if self.bg:
            surface.blit(self.bg, (0, 0))
        else:
            surface.fill((20, 20, 20))

        # title
        if self.title and self.title_font:
            ts = self.title_font.render(self.title, True, (255, 255, 255))
            tr = ts.get_rect()
            tr.centerx = surface.get_width() // 2
            tr.y = 20
            surface.blit(ts, tr)

        # stats
        surface.blit(self.font.render(f"Player: {self.life_player}", True, (200, 200, 200)), (40, 60))
        surface.blit(self.font.render(f"Enemy: {self.life_monster}", True, (200, 200, 200)), (40, 100))

        # options list
        base_x = 50
        base_y = surface.get_height() - 200
        for i, opt in enumerate(self.options):
            text = opt.get("text")
            color = (255, 255, 0) if i == self.player_selection and self.turn == 0 else (255, 255, 255)
            lbl = self.font.render(text, True, color)
            surface.blit(lbl, (base_x, base_y + i * 40))


SCENE_CLASS = BattleManager