<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import pygame
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import random
from scene import Scene
from ui import BattleHUD

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
        
        # Temp variables for enemy turn timing
        self._enemy_turn_timer = 0.0
        self._enemy_action_pending = False

    def enter(self):
        bg_path = self.data.get("background")
        self.bg = self.engine.load_image(bg_path)
        if self.bg:
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size())
        
        music_path = self.data.get("music")
        if music_path:
            self.engine.play_music(music_path, loop=-1)

        self.life_player = self.engine.state.get("player_hp", 10) # 10 es default
        self.player_skills = self.data.get("player", {}).get("skills", [])
        
        self.enemies = []
        for enemy_data in self.data.get("enemies", []):
            self.enemies.append({
                "id": enemy_data.get("id"),
                "type": enemy_data.get("type"),
                "hp": enemy_data.get("hp", 10),
                "max_hp": enemy_data.get("max_hp", 10),
                "skills": enemy_data.get("skills", []),
                "sprite": self.engine.load_image(enemy_data.get("sprite")),
                "pos": enemy_data.get("pos", [1500, 300])
            })
        
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
        """El jugador ha presionado Enter en una habilidad."""
        skill = self.player_skills[self.player_selection]
        
        if skill["type"] == "ATTACK":
            self.ui_state = "CHOOSE_TARGET" # Pasar a elegir objetivo
            self.target_selection = 0
        elif skill["type"] == "DEFEND":
            self.player_is_defending = True
            self._end_player_turn()
        elif skill["type"] == "ITEM_MENU":
            print("UI: Abriendo menú de items (no implementado)")
            # self.ui_state = "CHOOSE_ITEM"

    def _confirm_target(self):
        """El jugador ha presionado Enter en un objetivo."""
        skill = self.player_skills[self.player_selection]
        target = self.enemies[self.target_selection]
        
        # 1. Aplicar lógica de la habilidad
        if skill["type"] == "ATTACK":
            dmg = skill.get("dmg", 0)
            cost = skill.get("cost", 0)
            
            target["hp"] -= dmg
            self.life_player -= cost

            self.engine.play_sound("assets/sfx/punch_hit.ogg") # Efecto de sonido de golpe
            
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
        # Manejar el temporizador del turno enemigo
        if self._enemy_action_pending:
            self._enemy_turn_timer -= dt
            if self._enemy_turn_timer <= 0:
                self._execute_enemy_turn()

    def draw(self, surface):
        # 1. Fondo
        if self.bg:
            surface.blit(self.bg, (0, 0))
        else:
            surface.fill((20, 20, 20))
            
        # 2. Sprites (Capa de Actores)
        # (El AnimationManager podría manejar esto, pero por ahora lo dibujamos directo)
        for enemy in self.enemies:
            if enemy["sprite"]:
                surface.blit(enemy["sprite"], enemy["pos"])
                # Dibujar cursor de objetivo (si aplica)
                if self.ui_state == "CHOOSE_TARGET" and self.enemies[self.target_selection] == enemy:
                    pygame.draw.rect(surface, (255,0,0), (enemy["pos"][0], enemy["pos"][1] + 100, 50, 10), 2)


        # 3. UI (Capa de HUD)
        self.ui.draw(
            surface,
            player_hp=self.life_player,
            enemies=self.enemies,
            skills=self.player_skills,
            selected_skill_idx=self.player_selection
        )
        
=======
# Description: This module manages the battle scenes in the game.
import pygame, sys
=======
=======
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)
=======
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)
=======
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)
=======
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)
=======
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)
"""
Battle manager scene.

This Scene handles a very small turn-based battle where the player chooses
between two attacks. It accepts `monster_type` in `data` when the scene is
created or loaded (e.g. `scene_manager.load_scene('scripts.battle', data={'monster_type': 'rat'})`).
On victory/defeat it will try to load optional `victory` / `defeat` scene names
from the provided `data` dictionary.
"""

import pygame,sys
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)
=======
import pygame
>>>>>>> 6044657 (refactor: clean up comments and improve enemy initialization in BattleManager)
import os
=======
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
import random
from scene import Scene
from ui import BattleHUD

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
        
        # Temp variables for enemy turn timing
        self._enemy_turn_timer = 0.0
        self._enemy_action_pending = False

    def enter(self):
        bg_path = self.data.get("background")
        self.bg = self.engine.load_image(bg_path)
        if self.bg:
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size())
        
        music_path = self.data.get("music")
        if music_path:
            self.engine.play_music(music_path, loop=-1)

        self.life_player = self.engine.state.get("player_hp", 10) # 10 es default
        self.player_skills = self.data.get("player", {}).get("skills", [])
        
        self.enemies = []
        for enemy_data in self.data.get("enemies", []):
            self.enemies.append({
                "id": enemy_data.get("id"),
                "type": enemy_data.get("type"),
                "hp": enemy_data.get("hp", 10),
                "max_hp": enemy_data.get("max_hp", 10),
                "skills": enemy_data.get("skills", []),
                "sprite": self.engine.load_image(enemy_data.get("sprite")),
                "pos": enemy_data.get("pos", [1500, 300])
            })
        
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
        """El jugador ha presionado Enter en una habilidad."""
        skill = self.player_skills[self.player_selection]
        
        if skill["type"] == "ATTACK":
            self.ui_state = "CHOOSE_TARGET" # Pasar a elegir objetivo
            self.target_selection = 0
        elif skill["type"] == "DEFEND":
            self.player_is_defending = True
            self._end_player_turn()
        elif skill["type"] == "ITEM_MENU":
            print("UI: Abriendo menú de items (no implementado)")
            # self.ui_state = "CHOOSE_ITEM"

    def _confirm_target(self):
        """El jugador ha presionado Enter en un objetivo."""
        skill = self.player_skills[self.player_selection]
        target = self.enemies[self.target_selection]
        
        # 1. Aplicar lógica de la habilidad
        if skill["type"] == "ATTACK":
            dmg = skill.get("dmg", 0)
            cost = skill.get("cost", 0)
            
            target["hp"] -= dmg
            self.life_player -= cost

            self.engine.play_sound("assets/sfx/punch_hit.ogg") # Efecto de sonido de golpe
            
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
        # Manejar el temporizador del turno enemigo
        if self._enemy_action_pending:
            self._enemy_turn_timer -= dt
            if self._enemy_turn_timer <= 0:
                self._execute_enemy_turn()

    def draw(self, surface):
        # 1. Fondo
        if self.bg:
            surface.blit(self.bg, (0, 0))
        else:
            surface.fill((20, 20, 20))
            
        # 2. Sprites (Capa de Actores)
        # (El AnimationManager podría manejar esto, pero por ahora lo dibujamos directo)
        for enemy in self.enemies:
            if enemy["sprite"]:
                surface.blit(enemy["sprite"], enemy["pos"])
                # Dibujar cursor de objetivo (si aplica)
                if self.ui_state == "CHOOSE_TARGET" and self.enemies[self.target_selection] == enemy:
                    pygame.draw.rect(surface, (255,0,0), (enemy["pos"][0], enemy["pos"][1] + 100, 50, 10), 2)


<<<<<<< HEAD
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
=======
        # 3. UI (Capa de HUD)
        self.ui.draw(
            surface,
            player_hp=self.life_player,
            enemies=self.enemies,
            skills=self.player_skills,
            selected_skill_idx=self.player_selection
        )
        
<<<<<<< HEAD
        # (El TransitionManager dibuja el fundido encima de todo esto)


# ¡No olvidar registrar la clase!
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
SCENE_CLASS = BattleManager
=======
# Consult of HP, Status, Object, etc.
>>>>>>> 9dd9a3f (Editing the main - engine - escene_maganer files and configuring them and eliminating extra files. I'm trying to do the first escene)
=======
# Description: This module manages the battle scenes in the game.
import pygame, sys
=======
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)
=======
import pygame
>>>>>>> 6044657 (refactor: clean up comments and improve enemy initialization in BattleManager)
import os
=======
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
import random
from scene import Scene
from ui import BattleHUD

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
        
        # Temp variables for enemy turn timing
        self._enemy_turn_timer = 0.0
        self._enemy_action_pending = False

    def enter(self):
        bg_path = self.data.get("background")
        self.bg = self.engine.load_image(bg_path)
        if self.bg:
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size())
        
        music_path = self.data.get("music")
        if music_path:
            self.engine.play_music(music_path, loop=-1)

        self.life_player = self.engine.state.get("player_hp", 10) # 10 es default
        self.player_skills = self.data.get("player", {}).get("skills", [])
        
        self.enemies = []
        for enemy_data in self.data.get("enemies", []):
            self.enemies.append({
                "id": enemy_data.get("id"),
                "type": enemy_data.get("type"),
                "hp": enemy_data.get("hp", 10),
                "max_hp": enemy_data.get("max_hp", 10),
                "skills": enemy_data.get("skills", []),
                "sprite": self.engine.load_image(enemy_data.get("sprite")),
                "pos": enemy_data.get("pos", [1500, 300])
            })
        
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
        """El jugador ha presionado Enter en una habilidad."""
        skill = self.player_skills[self.player_selection]
        
        if skill["type"] == "ATTACK":
            self.ui_state = "CHOOSE_TARGET" # Pasar a elegir objetivo
            self.target_selection = 0
        elif skill["type"] == "DEFEND":
            self.player_is_defending = True
            self._end_player_turn()
        elif skill["type"] == "ITEM_MENU":
            print("UI: Abriendo menú de items (no implementado)")
            # self.ui_state = "CHOOSE_ITEM"

    def _confirm_target(self):
        """El jugador ha presionado Enter en un objetivo."""
        skill = self.player_skills[self.player_selection]
        target = self.enemies[self.target_selection]
        
        # 1. Aplicar lógica de la habilidad
        if skill["type"] == "ATTACK":
            dmg = skill.get("dmg", 0)
            cost = skill.get("cost", 0)
            
            target["hp"] -= dmg
            self.life_player -= cost

            self.engine.play_sound("assets/sfx/punch_hit.ogg") # Efecto de sonido de golpe
            
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
        # Manejar el temporizador del turno enemigo
        if self._enemy_action_pending:
            self._enemy_turn_timer -= dt
            if self._enemy_turn_timer <= 0:
                self._execute_enemy_turn()

    def draw(self, surface):
        # 1. Fondo
        if self.bg:
            surface.blit(self.bg, (0, 0))
        else:
            surface.fill((20, 20, 20))
            
        # 2. Sprites (Capa de Actores)
        # (El AnimationManager podría manejar esto, pero por ahora lo dibujamos directo)
        for enemy in self.enemies:
            if enemy["sprite"]:
                surface.blit(enemy["sprite"], enemy["pos"])
                # Dibujar cursor de objetivo (si aplica)
                if self.ui_state == "CHOOSE_TARGET" and self.enemies[self.target_selection] == enemy:
                    pygame.draw.rect(surface, (255,0,0), (enemy["pos"][0], enemy["pos"][1] + 100, 50, 10), 2)


<<<<<<< HEAD
SCENE_CLASS = BattleManager
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
=======
        # 3. UI (Capa de HUD)
        self.ui.draw(
            surface,
            player_hp=self.life_player,
            enemies=self.enemies,
            skills=self.player_skills,
            selected_skill_idx=self.player_selection
        )
        
<<<<<<< HEAD
        # (El TransitionManager dibuja el fundido encima de todo esto)


# ¡No olvidar registrar la clase!
SCENE_CLASS = BattleManager
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
=======
SCENE_CLASS = BattleManager
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
# Consult of HP, Status, Object, etc.
>>>>>>> 9dd9a3f (Editing the main - engine - escene_maganer files and configuring them and eliminating extra files. I'm trying to do the first escene)
=======
# Description: This module manages the battle scenes in the game.
import pygame, sys
=======
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)
=======
import pygame
>>>>>>> 6044657 (refactor: clean up comments and improve enemy initialization in BattleManager)
import os
=======
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
import random
from scene import Scene
from ui import BattleHUD

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
        
        # Temp variables for enemy turn timing
        self._enemy_turn_timer = 0.0
        self._enemy_action_pending = False

    def enter(self):
        bg_path = self.data.get("background")
        self.bg = self.engine.load_image(bg_path)
        if self.bg:
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size())
        
        music_path = self.data.get("music")
        if music_path:
            self.engine.play_music(music_path, loop=-1)

        self.life_player = self.engine.state.get("player_hp", 10) # 10 es default
        self.player_skills = self.data.get("player", {}).get("skills", [])
        
        self.enemies = []
        for enemy_data in self.data.get("enemies", []):
            self.enemies.append({
                "id": enemy_data.get("id"),
                "type": enemy_data.get("type"),
                "hp": enemy_data.get("hp", 10),
                "max_hp": enemy_data.get("max_hp", 10),
                "skills": enemy_data.get("skills", []),
                "sprite": self.engine.load_image(enemy_data.get("sprite")),
                "pos": enemy_data.get("pos", [1500, 300])
            })
        
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
        """El jugador ha presionado Enter en una habilidad."""
        skill = self.player_skills[self.player_selection]
        
        if skill["type"] == "ATTACK":
            self.ui_state = "CHOOSE_TARGET" # Pasar a elegir objetivo
            self.target_selection = 0
        elif skill["type"] == "DEFEND":
            self.player_is_defending = True
            self._end_player_turn()
        elif skill["type"] == "ITEM_MENU":
            print("UI: Abriendo menú de items (no implementado)")
            # self.ui_state = "CHOOSE_ITEM"

    def _confirm_target(self):
        """El jugador ha presionado Enter en un objetivo."""
        skill = self.player_skills[self.player_selection]
        target = self.enemies[self.target_selection]
        
        # 1. Aplicar lógica de la habilidad
        if skill["type"] == "ATTACK":
            dmg = skill.get("dmg", 0)
            cost = skill.get("cost", 0)
            
            target["hp"] -= dmg
            self.life_player -= cost

            self.engine.play_sound("assets/sfx/punch_hit.ogg") # Efecto de sonido de golpe
            
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
        # Manejar el temporizador del turno enemigo
        if self._enemy_action_pending:
            self._enemy_turn_timer -= dt
            if self._enemy_turn_timer <= 0:
                self._execute_enemy_turn()

    def draw(self, surface):
        # 1. Fondo
        if self.bg:
            surface.blit(self.bg, (0, 0))
        else:
            surface.fill((20, 20, 20))
            
        # 2. Sprites (Capa de Actores)
        # (El AnimationManager podría manejar esto, pero por ahora lo dibujamos directo)
        for enemy in self.enemies:
            if enemy["sprite"]:
                surface.blit(enemy["sprite"], enemy["pos"])
                # Dibujar cursor de objetivo (si aplica)
                if self.ui_state == "CHOOSE_TARGET" and self.enemies[self.target_selection] == enemy:
                    pygame.draw.rect(surface, (255,0,0), (enemy["pos"][0], enemy["pos"][1] + 100, 50, 10), 2)


<<<<<<< HEAD
SCENE_CLASS = BattleManager
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
=======
        # 3. UI (Capa de HUD)
        self.ui.draw(
            surface,
            player_hp=self.life_player,
            enemies=self.enemies,
            skills=self.player_skills,
            selected_skill_idx=self.player_selection
        )
        
<<<<<<< HEAD
        # (El TransitionManager dibuja el fundido encima de todo esto)


# ¡No olvidar registrar la clase!
SCENE_CLASS = BattleManager
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
=======
SCENE_CLASS = BattleManager
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
# Consult of HP, Status, Object, etc.
>>>>>>> 9dd9a3f (Editing the main - engine - escene_maganer files and configuring them and eliminating extra files. I'm trying to do the first escene)
=======
# Description: This module manages the battle scenes in the game.
import pygame, sys
=======
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)
=======
import pygame
>>>>>>> 6044657 (refactor: clean up comments and improve enemy initialization in BattleManager)
import os
=======
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
import random
from scene import Scene
from ui import BattleHUD

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
        
        # Temp variables for enemy turn timing
        self._enemy_turn_timer = 0.0
        self._enemy_action_pending = False

    def enter(self):
        bg_path = self.data.get("background")
        self.bg = self.engine.load_image(bg_path)
        if self.bg:
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size())
        
        music_path = self.data.get("music")
        if music_path:
            self.engine.play_music(music_path, loop=-1)

        self.life_player = self.engine.state.get("player_hp", 10) # 10 es default
        self.player_skills = self.data.get("player", {}).get("skills", [])
        
        self.enemies = []
        for enemy_data in self.data.get("enemies", []):
            self.enemies.append({
                "id": enemy_data.get("id"),
                "type": enemy_data.get("type"),
                "hp": enemy_data.get("hp", 10),
                "max_hp": enemy_data.get("max_hp", 10),
                "skills": enemy_data.get("skills", []),
                "sprite": self.engine.load_image(enemy_data.get("sprite")),
                "pos": enemy_data.get("pos", [1500, 300])
            })
        
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
        """El jugador ha presionado Enter en una habilidad."""
        skill = self.player_skills[self.player_selection]
        
        if skill["type"] == "ATTACK":
            self.ui_state = "CHOOSE_TARGET" # Pasar a elegir objetivo
            self.target_selection = 0
        elif skill["type"] == "DEFEND":
            self.player_is_defending = True
            self._end_player_turn()
        elif skill["type"] == "ITEM_MENU":
            print("UI: Abriendo menú de items (no implementado)")
            # self.ui_state = "CHOOSE_ITEM"

    def _confirm_target(self):
        """El jugador ha presionado Enter en un objetivo."""
        skill = self.player_skills[self.player_selection]
        target = self.enemies[self.target_selection]
        
        # 1. Aplicar lógica de la habilidad
        if skill["type"] == "ATTACK":
            dmg = skill.get("dmg", 0)
            cost = skill.get("cost", 0)
            
            target["hp"] -= dmg
            self.life_player -= cost

            self.engine.play_sound("assets/sfx/punch_hit.ogg") # Efecto de sonido de golpe
            
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
        # Manejar el temporizador del turno enemigo
        if self._enemy_action_pending:
            self._enemy_turn_timer -= dt
            if self._enemy_turn_timer <= 0:
                self._execute_enemy_turn()

    def draw(self, surface):
        # 1. Fondo
        if self.bg:
            surface.blit(self.bg, (0, 0))
        else:
            surface.fill((20, 20, 20))
            
        # 2. Sprites (Capa de Actores)
        # (El AnimationManager podría manejar esto, pero por ahora lo dibujamos directo)
        for enemy in self.enemies:
            if enemy["sprite"]:
                surface.blit(enemy["sprite"], enemy["pos"])
                # Dibujar cursor de objetivo (si aplica)
                if self.ui_state == "CHOOSE_TARGET" and self.enemies[self.target_selection] == enemy:
                    pygame.draw.rect(surface, (255,0,0), (enemy["pos"][0], enemy["pos"][1] + 100, 50, 10), 2)


<<<<<<< HEAD
SCENE_CLASS = BattleManager
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
=======
        # 3. UI (Capa de HUD)
        self.ui.draw(
            surface,
            player_hp=self.life_player,
            enemies=self.enemies,
            skills=self.player_skills,
            selected_skill_idx=self.player_selection
        )
        
<<<<<<< HEAD
        # (El TransitionManager dibuja el fundido encima de todo esto)


# ¡No olvidar registrar la clase!
SCENE_CLASS = BattleManager
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
=======
SCENE_CLASS = BattleManager
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
# Consult of HP, Status, Object, etc.
>>>>>>> 9dd9a3f (Editing the main - engine - escene_maganer files and configuring them and eliminating extra files. I'm trying to do the first escene)
=======
# Description: This module manages the battle scenes in the game.
import pygame, sys
=======
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)
=======
import pygame
>>>>>>> 6044657 (refactor: clean up comments and improve enemy initialization in BattleManager)
import os
=======
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
import random
from scene import Scene
from ui import BattleHUD

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
        
        # Temp variables for enemy turn timing
        self._enemy_turn_timer = 0.0
        self._enemy_action_pending = False

    def enter(self):
        bg_path = self.data.get("background")
        self.bg = self.engine.load_image(bg_path)
        if self.bg:
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size())
        
        music_path = self.data.get("music")
        if music_path:
            self.engine.play_music(music_path, loop=-1)

        self.life_player = self.engine.state.get("player_hp", 10) # 10 es default
        self.player_skills = self.data.get("player", {}).get("skills", [])
        
        self.enemies = []
        for enemy_data in self.data.get("enemies", []):
            self.enemies.append({
                "id": enemy_data.get("id"),
                "type": enemy_data.get("type"),
                "hp": enemy_data.get("hp", 10),
                "max_hp": enemy_data.get("max_hp", 10),
                "skills": enemy_data.get("skills", []),
                "sprite": self.engine.load_image(enemy_data.get("sprite")),
                "pos": enemy_data.get("pos", [1500, 300])
            })
        
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
        """El jugador ha presionado Enter en una habilidad."""
        skill = self.player_skills[self.player_selection]
        
        if skill["type"] == "ATTACK":
            self.ui_state = "CHOOSE_TARGET" # Pasar a elegir objetivo
            self.target_selection = 0
        elif skill["type"] == "DEFEND":
            self.player_is_defending = True
            self._end_player_turn()
        elif skill["type"] == "ITEM_MENU":
            print("UI: Abriendo menú de items (no implementado)")
            # self.ui_state = "CHOOSE_ITEM"

    def _confirm_target(self):
        """El jugador ha presionado Enter en un objetivo."""
        skill = self.player_skills[self.player_selection]
        target = self.enemies[self.target_selection]
        
        # 1. Aplicar lógica de la habilidad
        if skill["type"] == "ATTACK":
            dmg = skill.get("dmg", 0)
            cost = skill.get("cost", 0)
            
            target["hp"] -= dmg
            self.life_player -= cost

            self.engine.play_sound("assets/sfx/punch_hit.ogg") # Efecto de sonido de golpe
            
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
        # Manejar el temporizador del turno enemigo
        if self._enemy_action_pending:
            self._enemy_turn_timer -= dt
            if self._enemy_turn_timer <= 0:
                self._execute_enemy_turn()

    def draw(self, surface):
        # 1. Fondo
        if self.bg:
            surface.blit(self.bg, (0, 0))
        else:
            surface.fill((20, 20, 20))
            
        # 2. Sprites (Capa de Actores)
        # (El AnimationManager podría manejar esto, pero por ahora lo dibujamos directo)
        for enemy in self.enemies:
            if enemy["sprite"]:
                surface.blit(enemy["sprite"], enemy["pos"])
                # Dibujar cursor de objetivo (si aplica)
                if self.ui_state == "CHOOSE_TARGET" and self.enemies[self.target_selection] == enemy:
                    pygame.draw.rect(surface, (255,0,0), (enemy["pos"][0], enemy["pos"][1] + 100, 50, 10), 2)


<<<<<<< HEAD
SCENE_CLASS = BattleManager
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
=======
        # 3. UI (Capa de HUD)
        self.ui.draw(
            surface,
            player_hp=self.life_player,
            enemies=self.enemies,
            skills=self.player_skills,
            selected_skill_idx=self.player_selection
        )
        
<<<<<<< HEAD
        # (El TransitionManager dibuja el fundido encima de todo esto)


# ¡No olvidar registrar la clase!
SCENE_CLASS = BattleManager
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
=======
SCENE_CLASS = BattleManager
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
# Consult of HP, Status, Object, etc.
>>>>>>> 9dd9a3f (Editing the main - engine - escene_maganer files and configuring them and eliminating extra files. I'm trying to do the first escene)
=======
# Description: This module manages the battle scenes in the game.
import pygame, sys
=======
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)
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
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
