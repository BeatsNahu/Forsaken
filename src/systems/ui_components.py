import pygame
import os
import config

class DialogueBox:
    def __init__(self, engine, image_path="assets/ui/box_dialogue.png"):
        self.engine = engine
        
        # Load the dialogue box image
        original_image = self.engine.load_image(image_path)
        
        # Load fonts
        font_path = config.FONT_PATH_DEFAULT
        self.font = self.engine.load_font(font_path, config.FONT_SIZE_REGULAR)
        self.speaker_font = self.engine.load_font(font_path, config.FONT_SIZE_SPEAKER)

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
        self.text_speed = config.TEXT_SPEED_DEFAULT  # characters per second
        self.current_full_text = ""  
        self.visible_chars = 0.0 # Float for smooth typing
        self.text_timer = 0.0 # Timer to track elapsed time
        self.is_typing = False

        # Fade variables
        self.alpha = 0.0           
        self.target_alpha = 0.0    
        self.fade_speed = config.FADE_SPEED_DEFAULT

        # SFX of typing
        self.typing_sfx_path = config.SFX_UI_TYPING
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

        # Colors
        text_default = config.COLOR_WHITE
        text_selected_color = config.COLOR_YELLOW
        text_speaker_color = config.COLOR_YELLOW

        # Draw choices if provided
        if choices:
            self.is_typing = False
            for i, c in enumerate(choices):
                text_c = c.get("text") or str(c)
                color = text_selected_color if i == choice_idx else text_default
                
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
                spk_surf = self.speaker_font.render(f"{speaker}:", True, text_speaker_color)
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
    def __init__(self, engine, choices_list: list, ui_config: dict = None):
        self.engine = engine
        self.choices = choices_list
        self.selected_idx = 0

        # Diccionario de configuración (¡Data-Driven!)
        self.config = ui_config or {}

        # 1. Cargar imagen de fondo
        image_path = self.config.get("image", "assets/ui/box_choice.png") # Imagen por defecto
        self.box_image_orig = self.engine.load_image(image_path)
        
        # (Aquí puedes añadir lógica para escalar self.box_image_orig si es necesario)
        self.box_image = self.box_image_orig 

        # 2. Cargar fuentes (con fallback a config)
        font_path = self.config.get("font_path", config.FONT_PATH_DEFAULT)
        font_size = self.config.get("font_size", config.FONT_SIZE_REGULAR)
        self.font = self.engine.load_font(font_path, font_size)

        # 3. Cargar sonidos (con fallback a config)
        self.sfx_swap = self.config.get("sfx_swap", config.SFX_UI_SWAP)
        self.sfx_confirm = self.config.get("sfx_confirm", config.SFX_UI_CONFIRM)

        # 4. Posición (con fallback)
        self.x = self.config.get("pos_x", 100)
        self.y = self.config.get("pos_y", 100)
        
        # 5. Layout (padding interno)
        self.padding = self.config.get("padding", 40)
        self.line_spacing = self.config.get("line_spacing", 15)

        # 6. Variables de Fade (¡propias!)
        self.alpha = 0.0
        self.target_alpha = 0.0
        self.fade_speed = self.config.get("fade_speed", config.FADE_SPEED_DEFAULT)

    def handle_event(self, event):
        """Gestiona solo la navegación (Arriba/Abajo)"""
        if event.key == pygame.K_DOWN:
            self.selected_idx = (self.selected_idx + 1) % len(self.choices)
            self.engine.play_sound(self.sfx_swap)
        elif event.key == pygame.K_UP:
            self.selected_idx = (self.selected_idx - 1) % len(self.choices)
            self.engine.play_sound(self.sfx_swap)

    def get_selected_choice(self):
        """Devuelve la opción (diccionario) que está seleccionada."""
        if 0 <= self.selected_idx < len(self.choices):
            return self.choices[self.selected_idx]
        return None
    
    def update(self, dt):
        """Actualiza el efecto de fundido (fade)."""
        if self.alpha != self.target_alpha:
            if self.alpha < self.target_alpha:
                self.alpha += self.fade_speed * dt
                if self.alpha >= self.target_alpha:
                    self.alpha = self.target_alpha
            else:
                self.alpha -= self.fade_speed * dt
                if self.alpha <= self.target_alpha:
                    self.alpha = self.target_alpha

    def draw(self, surface):
        """Dibuja la caja de opciones y el texto."""
        if self.alpha == 0:
            return  # Totalmente transparente
        
        # 1. Dibujar la imagen de fondo de la caja
        if self.box_image:
            self.box_image.set_alpha(self.alpha)
            surface.blit(self.box_image, (self.x, self.y))

        # 2. Definir posición inicial del texto
        current_y = self.y + self.padding
        text_x = self.x + self.padding
        
        # 3. Dibujar cada opción
        for i, choice in enumerate(self.choices):
            text = choice.get("text", "Opción")
            
            # Resaltar la opción seleccionada
            color = config.COLOR_YELLOW if i == self.selected_idx else config.COLOR_WHITE
            
            # Renderizar el texto
            text_surf = self.font.render(text, True, color)
            text_surf.set_alpha(self.alpha)
            
            # Dibujar en la pantalla
            surface.blit(text_surf, (text_x, current_y))
            
            # Mover la "Y" para la siguiente línea
            current_y += self.font.get_height() + self.line_spacing

    def fade_in(self):
        self.target_alpha = 255.0

    def fade_out(self):
        self.target_alpha = 0.0

    def is_fade_complete(self):
        return self.alpha == self.target_alpha
    
class BattleHUD:
    def __init__(self, engine):
        self.engine = engine

        # Load fonts
        font_path = config.FONT_PATH_DEFAULT
        self.font = self.engine.load_font(font_path, config.FONT_SIZE_HUD)
        self.hp_font = self.engine.load_font(font_path, config.FONT_SIZE_HUD_HP)

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
        
        # 1. Definir colores
        color_selected = config.COLOR_YELLOW
        color_default = config.COLOR_WHITE
        color_hp = config.COLOR_RED
    
        # Draw stats panel
        if self.pos_stats_panel:
            base_x = self.pos_stats_panel[0] + config.BATTLE_HUD_PADDING_X
            base_y = self.pos_stats_panel[1]   
            skill_base_y = base_y + config.BATTLE_HUD_SKILL_START_Y
            line_spacing = config.BATTLE_HUD_LINE_SPACING
            hp_pos = (base_x, base_y + config.BATTLE_HUD_HP_POS_Y)
        
        else:
            # Fallback si no hay panel
            base_x = config.BATTLE_HUD_FALLBACK_BASE_X
            skill_base_y = config.BATTLE_HUD_FALLBACK_BASE_Y
            hp_pos = (config.BATTLE_HUD_FALLBACK_HP_POS_X, config.BATTLE_HUD_FALLBACK_HP_POS_Y)
            line_spacing = config.BATTLE_HUD_FALLBACK_SPACING

        # 2. Dibujar el panel
        if self.img_stats_panel:
            surface.blit(self.img_stats_panel, self.pos_stats_panel)
        
        # 3. Dibujar HP del Jugador
        surface.blit(self.hp_font.render(f"Player HP: {player_hp}", True, color_hp), hp_pos)

        # 4. Dibujar Habilidades
        for i, skill in enumerate(skills):
            text = skill.get("text")
            color = color_selected if i == selected_skill_idx else color_default
            lbl = self.font.render(text, True, color)
            surface.blit(lbl, (base_x, skill_base_y + i * line_spacing))

class ChapterTitle:
    def __init__(self, engine, text, duration=3.0, fade_time=0.5):
        # Initialize chapter title 
        self.engine = engine
        self.text = text
        self.timer = duration # 1.5 seconds
        self.lifetime = 0.0 # Total time since start
        self.fade_time = fade_time # Time for fade in/out
        # Load font
        font_path = config.FONT_PATH_DEFAULT
        self.font = self.engine.load_font(font_path, config.FONT_SIZE_TITLE)
        
        # Typing effect variables
        self.text_speed = config.TEXT_SPEED_DEFAULT  # characters per second
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