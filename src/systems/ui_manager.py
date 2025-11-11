import pygame
import os

class DialogueBox:
    def __init__(self, engine, image_path="assets/ui/box_dialogue.png"):
        self.engine = engine
        
        # Load the dialogue box image
        original_image = self.engine.load_image(image_path)
        
        # Load fonts
        font_path = os.path.join("assets", "fonts", "press-start.k.ttf")
        font_path = font_path if os.path.exists(font_path) else None
        self.font = self.engine.load_font(font_path, 20)
        self.speaker_font = self.engine.load_font(font_path, 24)
        
        # Resize image to fit screen width
        if original_image:
            target_width = int(self.engine.screen.get_size()[0] * 0.85)
            
            # Maintain aspect ratio
            original_width, original_height = original_image.get_size()
            aspect_ratio = original_height / original_width
            target_height = int(target_width * aspect_ratio)
            
            # Scale image
            self.box_image = pygame.transform.scale(original_image, (target_width, target_height))
            
            # Center the box at the bottom of the screen
            self.x = (self.engine.screen.get_width() - self.box_image.get_width()) // 2
            self.y = self.engine.screen.get_height() - self.box_image.get_height() - 100
        
        else:
            # Fallback if image not found
            self.box_image = None
            self.x, self.y = 50, engine.screen.get_height()

        # Layout positions
        self.speaker_pos = (self.x + 130, self.y + 630)
        self.text_pos = (self.x + 160, self.y + 720)
        self.choice_pos = (self.x + 160, self.y + 750) 

        # Typing effect variables
        self.text_speed = 30  # characters per second
        self.current_full_text = ""  
        self.visible_chars = 0.0 # Float for smooth typing
        self.text_timer = 0.0 # Timer to track elapsed time
        self.is_typing = False

        # Fade variables
        self.alpha = 0.0           
        self.target_alpha = 0.0    
        self.fade_speed = 400.0

        # SFX of typing
        self.typing_sfx_path = "assets/audio/sfx/type_writing1.ogg"
        self.last_char_sound = 0

    def update(self, dt):
        # Update typing effect
        self.text_timer += dt

        if self.is_typing:
            self.visible_chars = self.text_timer * self.text_speed # characters to show

            # Logic to play typing sound effect
            if int(self.visible_chars) > self.last_char_sound:
                self.last_char_sound = int(self.visible_chars)
                self.engine.play_sound(self.typing_sfx_path, volume=0.3)
            # Logic to finish typing
            if self.visible_chars >= len(self.current_full_text):
                self.is_typing = False
                self.visible_chars = len(self.current_full_text)

        # Update fade effect
        if self.alpha != self.target_alpha:
            if self.alpha < self.target_alpha:
                self.alpha += self.fade_speed * dt
                if self.alpha >= self.target_alpha:
                    self.alpha = self.target_alpha
            else:
                self.alpha -= self.fade_speed * dt
                if self.alpha <= self.target_alpha:
                    self.alpha = self.target_alpha

    def draw(self, surface, text, speaker=None, choices=None, choice_idx=0):
        # Skip drawing
        if self.alpha == 0:
            return  # Fully transparent, nothing to draw
        
        # Draw dialogue box
        if self.box_image:
            self.box_image.set_alpha(self.alpha) # Set transparency
            surface.blit(self.box_image, (self.x, self.y))
        else:
            # Fallback (no soporta alfa, pero es raro)
            pygame.draw.rect(surface, (10, 10, 40), (self.x, self.y, 800, 150))

        # Draw choices if provided
        if choices:
            self.is_typing = False
            for i, c in enumerate(choices):
                text_c = c.get("text") or str(c)
                color = (255, 255, 0) if i == choice_idx else (255, 255, 255)
                
                # Render choice text
                surf = self.font.render(text_c, True, color)
                # Apply alpha
                surf.set_alpha(self.alpha)
                surface.blit(surf, (self.choice_pos[0], self.choice_pos[1] + i * 40))
        
        # Draw speaker and text
        elif text:
            # Check if new text to display
            if text != self.current_full_text:
                self.current_full_text = text
                self.visible_chars = 0.0
                self.text_timer = 0.0
                self.is_typing = True
                self.last_char_sound = 0
            
            # Show speaker name if provided
            if speaker and self.speaker_font:
                spk_surf = self.speaker_font.render(f"{speaker}:", True, (255, 255, 0))
                spk_surf.set_alpha(self.alpha) # Apply alpha
                surface.blit(spk_surf, self.speaker_pos)
            
            # Draw text with typing effect
            if self.font:
                visible_text = self.current_full_text[0 : int(self.visible_chars)]
                txt_surf = self.font.render(visible_text, True, (255, 255, 255))
                txt_surf.set_alpha(self.alpha) # Apply alpha
                surface.blit(txt_surf, self.text_pos)

    def skip_typing(self):
        self.visible_chars = len(self.current_full_text)
        self.is_typing = False

    def is_finished(self):
        return not self.is_typing
    
    def fade_in(self):
        self.target_alpha = 255.0

    def fade_out(self):
        self.target_alpha = 0.0

    def is_fade_complete(self):
        return self.alpha == self.target_alpha
    
class ChoiceBox:
    def __init__(self, engine):
        self.engine = engine
        # For simplicity, we can use DialogueBox for choices as well
        self.dialogue_box = DialogueBox(engine)

    def update(self, dt):
        self.dialogue_box.update(dt)

    def draw(self, surface, choices, selected_idx):
        self.dialogue_box.draw(surface, text=None, choices=choices, choice_idx=selected_idx)

    def fade_in(self):
        self.dialogue_box.fade_in()

    def fade_out(self):
        self.dialogue_box.fade_out()

    def is_fade_complete(self):
        return self.dialogue_box.is_fade_complete()
    
class BattleHUD:
    def __init__(self, engine):
        self.engine = engine

        # Load fonts
        font_path = os.path.join("assets", "fonts", "press-start.k.ttf")
        font_path = font_path if os.path.exists(font_path) else None
        self.font = self.engine.load_font(font_path, 28)
        self.hp_font = self.engine.load_font(font_path, 20)
        
        # Load stats panel image
        self.img_stats_panel = self.engine.load_image("assets/ui/battle/panel_stats.png")
        if self.img_stats_panel:
            # 1. Definir un ancho (ej: 90% de la pantalla)
            target_width = int(self.engine.screen.get_width() * 0.9)
            
            # 2. Calcular altura proporcional
            orig_w, orig_h = self.img_stats_panel.get_size()
            aspect_ratio = orig_h / orig_w if orig_w > 0 else 0
            target_height = int(target_width * aspect_ratio)
            
            # 3. Escalar la imagen
            self.img_stats_panel = pygame.transform.scale(self.img_stats_panel, (target_width, target_height))
            
            # 4. Posicionarla (ej: centrada abajo)
            self.pos_stats_panel = (
                (self.engine.screen.get_width() - self.img_stats_panel.get_width()) // 2,
                self.engine.screen.get_height() - self.img_stats_panel.get_height() - 20 
            )
        else:
            self.pos_stats_panel = None # Fallback

    def draw(self, surface, player_hp, enemies, skills, selected_skill_idx):
        
        # Draw stats panel
        if self.pos_stats_panel:
            # Posiciones relativas al panel
            base_x = self.pos_stats_panel[0] + 40
            skill_base_y = self.pos_stats_panel[1] + 100 
            hp_pos = (base_x, self.pos_stats_panel[1] + 50)
        else:
            # Fallback si no hay panel
            base_x = 50
            skill_base_y = surface.get_height() - 200
            hp_pos = (50, 50) # Fallback HP

        # 2. Dibujar el panel
        if self.img_stats_panel:
            surface.blit(self.img_stats_panel, self.pos_stats_panel)
        
        # 3. Dibujar HP del Jugador
        surface.blit(self.hp_font.render(f"Player HP: {player_hp}", True, (255, 255, 255)), hp_pos) #
        
        # 4. Dibujar Habilidades
        for i, skill in enumerate(skills):
            text = skill.get("text")
            color = (255, 255, 0) if i == selected_skill_idx else (255, 255, 255)
            lbl = self.font.render(text, True, color)
            surface.blit(lbl, (base_x, skill_base_y + i * 40))
class ChapterTitle:
    def __init__(self, engine, text, duration=3.0, fade_time=0.5):
        # Initialize chapter title 
        self.engine = engine
        self.text = text
        self.timer = duration # 1.5 seconds
        self.lifetime = 0.0 # Total time since start
        self.fade_time = fade_time # Time for fade in/out
        # Load font
        font_path = os.path.join("assets", "fonts", "press-start.k.ttf")
        font_path = font_path if os.path.exists(font_path) else None
        self.font = self.engine.load_font(font_path, 50)
        
        # Typing effect variables
        self.text_speed = 40  # characters per second
        self.visible_chars = 0.0 # Float for smooth typing
        self.text_timer = 0.0 # Timer to track elapsed time
        self.is_typing = True 
        self.text_surf = None
        self.pos = (0, 0) # Initialize position


    def update(self, dt):
        # For fade effect and typing effect
        if self.timer > 0:
            self.timer -= dt
            self.lifetime += dt

        # Typing effect
        if self.is_typing:
            self.text_timer += dt
            self.visible_chars = self.text_timer * self.text_speed
            # Render text surface
            if self.visible_chars >= len(self.text):
                self.is_typing = False
                self.visible_chars = len(self.text)

    def draw(self, surface):
        if self.timer <= 0:
            return
            
        # --- LÓGICA DE FUNDIDO CORREGIDA ---
        # Alfa de Fundido de Entrada (basado en lifetime)
        alpha_in = min(200, (self.lifetime / self.fade_time) * 200)
        # Alfa de Fundido de Salida (basado en timer)
        alpha_out = min(200, (self.timer / self.fade_time) * 200)
        # El alfa final es el más restrictivo (el más bajo)
        alpha = min(alpha_in, alpha_out)
        alpha = max(0, alpha) # Asegurarse que no sea negativo
        
        # Dibuja el velo negro
        s = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        s.fill((0, 0, 0, alpha))
        surface.blit(s, (0, 0))
        
        # --- Lógica de dibujado de texto (sin cambios) ---
        visible_text = self.text[0 : int(self.visible_chars)]
        self.text_surf = self.font.render(visible_text, True, (255, 255, 255))
        self.pos = (
            (self.engine.screen.get_width() - self.text_surf.get_width()) // 2,
            (self.engine.screen.get_height() - self.text_surf.get_height()) // 2
        )
        
        text_alpha = min(255, alpha * 1.275) # (255 / 200 = 1.275)
        self.text_surf.set_alpha(text_alpha)
        
        surface.blit(self.text_surf, self.pos)
            
    def is_finished(self):
        return self.timer <= 0