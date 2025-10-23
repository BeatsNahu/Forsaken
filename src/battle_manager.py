# Description: This module manages the battle scenes in the game.
import pygame, sys
import os
from scene import Scene
from ramdom import randint

class BattleManager:
    def __init__(self, engine):
        super().__init__(engine, {"id": "battle_manager"}) # Call the parent constructor with the engine and scene data
        # Define battle options
        self.options = [
            {"text": "Strong Punch (3 dmg, -1 player hp)"},
            {"text": "Weak Kick (1 dmg, +1 player hp)"}
        ]
        # Set initial battle parameters
        self.player_selection = 0 # Selected option index
        self.life_player = 10 # Player life
        self.life_monster = None # Monster life depends on monster type
        self.turn = randint(0, 1)  # 0 for player, 1 for monster
        self.monster_type = None # Type of monster
        self.attack_damage = None # Damage of the monster's attack
        self.punch = 3 # Strong attack damage
        self.kick = 1 # Weak attack damage

        # Preload fonts via engine cache to avoid recreating them every frame
        font_path = os.path.join("assets", "fonts", "press-start.k.ttf")
        self._font_path = font_path
        try: 
            self.font = self.engine.load_font(self._font_path, 30)
        except Exception:
            self.font = pygame.font.Font(self._font_path if os.path.exists(self._font_path) else None, 30)
        
        self.bg = None # Background image
        self.title = "Battle Scene" # Title text

    def enter(self):
        try:
            self.bg = pygame.image.load("assets/backgrounds/battle_scene.png").convert() # Load the battle background image
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size()) # Scale the image to fit the screen
        except Exception: # If there is an error loading the image
            self.bg = None

    def start_battle(self, monster_type):
        self.monster_type = monster_type
        if monster_type == "rat":
            self.life_monster = 10
            self.attack_damage = (3, 1)
        elif monster_type == "frog":
            self.life_monster = 11
            self.attack_damage = (3, 1)
        elif monster_type == "knife_guy":
            self.life_monster = 12
            self.attack_damage = (1, 4)
        self.turn = randint(0, 1)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_1:
                if self.monster_type and self.turn == 0:
                    print("Strong punch selected")
                    self.life_monster -= self.punch # Damage to monster
                    self.life_player -= 1 # Player takes slight damage
                    self.turn = 1  # Switch to monster's turn
            elif event.key == pygame.K_2:
                if self.monster_type and self.turn == 0:
                    print("Weak kick selected")
                    self.life_monster -= self.kick # Damage to monster
                    self.life_player += 1 # Heal player slightly
                    self.turn = 1  # Switch to monster's turn
                    

    def draw(self, surface):
        if self.bg:
            surface.blit(self.bg, (0, 0)) # Draw the background image
        
        # Options display
        for i, opt in enumerate(options):
            color = (255, 255, 0) if i == self.player_selection else (255, 255, 255)
            label = self.font.render(opt, True, color) # Render the option text
            surface.blit(label, {50, 500 + i * 40}) # Draw the option

        surface.blit(self.font.render(f"Player Life: {self.life_player}", True, (255, 255, 255)), (50, 50))
        surface.blit(self.font.render(f"Monster Life: {self.life_monster}", True, (255, 255, 255)), (50, 100))


SCENE_CLASS = BattleManager