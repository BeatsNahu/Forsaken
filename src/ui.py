<<<<<<< HEAD
<<<<<<< HEAD
import pygame
import os

class DialogueBox:
    def __init__(self, engine, image_path="assets/UI/Box_dialogue.png"):
        self.engine = engine
        
        # 1
        original_image = self.engine.load_image(image_path)
        
        # 2
        font_path = os.path.join("assets", "fonts", "press-start.k.ttf")
        font_path = font_path if os.path.exists(font_path) else None
        self.font = self.engine.load_font(font_path, 20)
        self.speaker_font = self.engine.load_font(font_path, 24)
        
        # 3
        if original_image:
            target_width = int(self.engine.screen.get_size()[0] * 0.85)
            
            # 
            original_width, original_height = original_image.get_size()
            aspect_ratio = original_height / original_width
            target_height = int(target_width * aspect_ratio)
            
            # 
            self.box_image = pygame.transform.scale(original_image, (target_width, target_height))
            
            #
            self.x = (self.engine.screen.get_width() - self.box_image.get_width()) // 2
            self.y = self.engine.screen.get_height() - self.box_image.get_height() - 100
        
        else:
            #
            self.box_image = None
            self.x, self.y = 50, engine.screen.get_height()

        #
        self.speaker_pos = (self.x + 130, self.y + 630)
        self.text_pos = (self.x + 160, self.y + 720)
        self.choice_pos = (self.x + 160, self.y + 750) #

    def draw(self, surface, text, speaker=None, choices=None, choice_idx=0):
        # 
=======
# ui.py
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
import pygame
import os

class DialogueBox:
    def __init__(self, engine, image_path="assets/UI/Box_dialogue.png"):
        self.engine = engine
        
        # 1
        original_image = self.engine.load_image(image_path)
        
        # 2
        font_path = os.path.join("assets", "fonts", "press-start.k.ttf")
        font_path = font_path if os.path.exists(font_path) else None
        self.font = self.engine.load_font(font_path, 20)
        self.speaker_font = self.engine.load_font(font_path, 24)
        
        # 3
        if original_image:
            target_width = int(self.engine.screen.get_size()[0] * 0.85)
            
            # 
            original_width, original_height = original_image.get_size()
            aspect_ratio = original_height / original_width
            target_height = int(target_width * aspect_ratio)
            
            # 
            self.box_image = pygame.transform.scale(original_image, (target_width, target_height))
            
            #
            self.x = (self.engine.screen.get_width() - self.box_image.get_width()) // 2
            self.y = self.engine.screen.get_height() - self.box_image.get_height() - 100
        
        else:
            #
            self.box_image = None
            self.x, self.y = 50, engine.screen.get_height()

        #
        self.speaker_pos = (self.x + 130, self.y + 630)
        self.text_pos = (self.x + 160, self.y + 720)
        self.choice_pos = (self.x + 160, self.y + 750) #

    def draw(self, surface, text, speaker=None, choices=None, choice_idx=0):
<<<<<<< HEAD
        """
        El método principal. scene.py solo llama a este.
        """
        # 1. Dibujar el recuadro
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
        # 
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        if self.box_image:
            surface.blit(self.box_image, (self.x, self.y))
        else:
            pygame.draw.rect(surface, (10, 10, 40), (self.x, self.y, 800, 150))

<<<<<<< HEAD
<<<<<<< HEAD
        # 
=======
        # 2. Dibujar elecciones (si las hay)
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
        # 
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        if choices:
            for i, c in enumerate(choices):
                text_c = c.get("text") or str(c)
                color = (255, 255, 0) if i == choice_idx else (255, 255, 255)
                surf = self.font.render(text_c, True, color)
                surface.blit(surf, (self.choice_pos[0], self.choice_pos[1] + i * 40))
        
<<<<<<< HEAD
<<<<<<< HEAD
        # 
=======
        # 3. Dibujar texto de diálogo (si no hay elecciones)
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
        # 
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        elif text:
            if speaker and self.speaker_font:
                spk_surf = self.speaker_font.render(f"{speaker}:", True, (255, 255, 0))
                surface.blit(spk_surf, self.speaker_pos)
            
            if self.font:
                txt_surf = self.font.render(text, True, (255, 255, 255))
                surface.blit(txt_surf, self.text_pos)

<<<<<<< HEAD
<<<<<<< HEAD
class BattleHUD:
    def __init__(self, engine):
        self.engine = engine
=======
# ---------------------------------------------------------------------------
# CLASE 2: El HUD de batalla (para battle_manager.py)
# ---------------------------------------------------------------------------
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
class BattleHUD:
    def __init__(self, engine):
        self.engine = engine
<<<<<<< HEAD
        
        # Carga sus propias fuentes (usando el caché)
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        font_path = os.path.join("assets", "fonts", "press-start.k.ttf")
        font_path = font_path if os.path.exists(font_path) else None
        self.font = self.engine.load_font(font_path, 28)
        self.hp_font = self.engine.load_font(font_path, 20)
        
<<<<<<< HEAD
<<<<<<< HEAD
=======
        # Carga sus propios recuadros (usando el caché)
        # self.menu_bg = self.engine.load_image("assets/ui/battle_menu_bg.png")

>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
    def draw(self, surface, player_hp, enemies, skills, selected_skill_idx):
        # ... (Aquí va toda la lógica de draw() que tenías en battle_manager.py)
        # 1. Dibujar Stats
        surface.blit(self.hp_font.render(f"Player HP: {player_hp}", True, (255, 255, 255)), (50, 50))
        
        for i, enemy in enumerate(enemies):
            hp_text = f"{enemy['type']} HP: {enemy['hp']}"
            surface.blit(self.hp_font.render(hp_text, True, (255, 100, 100)), (1500, 50 + i * 40))

        # 2. Dibujar Menú de Acciones
        base_x = 50
        base_y = surface.get_height() - 200
        for i, skill in enumerate(skills):
            text = skill.get("text")
            color = (255, 255, 0) if i == selected_skill_idx else (255, 255, 255)
            lbl = self.font.render(text, True, color)
            surface.blit(lbl, (base_x, base_y + i * 40))

<<<<<<< HEAD
<<<<<<< HEAD
class ChapterTitle:
    def __init__(self, engine, text, duration=1.5):
        self.engine = engine
        self.text = text
        self.timer = duration # 1.5 seconds
        
=======
# ---------------------------------------------------------------------------
# CLASE 3: Tu idea - El título de capítulo (Temporal)
# ---------------------------------------------------------------------------
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
class ChapterTitle:
    def __init__(self, engine, text, duration=1.5):
        self.engine = engine
        self.text = text
        self.timer = duration # 1.5 seconds
        
<<<<<<< HEAD
        # Carga su fuente (usando el caché)
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        font_path = os.path.join("assets", "fonts", "press-start.k.ttf")
        font_path = font_path if os.path.exists(font_path) else None
        self.font = self.engine.load_font(font_path, 50)
        
<<<<<<< HEAD
<<<<<<< HEAD
=======
        # Pre-renderiza el texto (porque no cambia)
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        self.text_surf = self.font.render(self.text, True, (255, 255, 255))
        self.pos = (
            (engine.screen.get_width() - self.text_surf.get_width()) // 2,
            (engine.screen.get_height() - self.text_surf.get_height()) // 2
        )

    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt

    def draw(self, surface):
        if self.timer > 0:
<<<<<<< HEAD
<<<<<<< HEAD
            # Draw fade effect
=======
            # Dibuja un fondo negro semitransparente
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
            # Draw fade effect
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
            s = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
            alpha = min(200, (self.timer / 1.5) * 200) # Fade out
            s.fill((0, 0, 0, alpha))
            surface.blit(s, (0, 0))
            
<<<<<<< HEAD
<<<<<<< HEAD
            # Draw text
            surface.blit(self.text_surf, self.pos)

            # Draw surface on top
            

=======
            # Dibuja el texto
            surface.blit(self.text_surf, self.pos)

>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
            # Draw text
            surface.blit(self.text_surf, self.pos)

            # Draw surface on top
            

>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
    def is_finished(self):
        return self.timer <= 0