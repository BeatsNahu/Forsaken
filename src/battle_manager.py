"""
Battle manager scene.

This Scene handles a very small turn-based battle where the player chooses
between two attacks. It accepts `monster_type` in `data` when the scene is
created or loaded (e.g. `scene_manager.load_scene('scripts.battle', data={'monster_type': 'rat'})`).
On victory/defeat it will try to load optional `victory` / `defeat` scene names
from the provided `data` dictionary.
"""

import pygame,sys
import os
import random
from scene import Scene


class BattleManager(Scene):
    def __init__(self, engine, data=None):
        super().__init__(engine, data or {"id": "battle_manager"})

        # Player choices
        self.options = [
            {"text": "1) Strong Punch (3 dmg, -1 player hp)"},
            {"text": "2) Weak Kick (1 dmg, +1 player hp)"},
        ]

        # Runtime state
        self.player_selection = 0
        self.life_player = 10
        self.life_monster = 0
        self.turn = 0  # 0: player, 1: monster
        self.monster_type = None
        self.attack_damage = (1, 2)
        self.punch = 3
        self.kick = 1

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
        # load background if available
        try:
            self.bg = pygame.image.load("assets/backgrounds/battle_scene.png").convert()
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size())
        except Exception:
            self.bg = None

        # If the scene was created with data specifying a monster, start it
        mt = self.data.get("monster_type")
        if mt:
            self.start_battle(mt)

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