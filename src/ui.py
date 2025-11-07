import pygame
import os

class DialogueBox:
    def __init__(self, engine, image_path="assets/UI/Box_dialogue.png"):
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

    def update(self, dt):
        if self.is_typing:
            self.text_timer += dt # Increment timer by delta time
            self.visible_chars = self.text_timer * self.text_speed # Calculate number of visible characters based on time and speed
            
            if self.visible_chars >= len(self.current_full_text): # All characters are visible
                self.is_typing = False # Stop typing effect
                self.visible_chars = len(self.current_full_text) # Clamp to full length

    def draw(self, surface, text, speaker=None, choices=None, choice_idx=0):
        # Draw dialogue box
        if self.box_image:
            surface.blit(self.box_image, (self.x, self.y))
        else:
            pygame.draw.rect(surface, (10, 10, 40), (self.x, self.y, 800, 150))

        # Draw choices if provided
        if choices:
            for i, c in enumerate(choices):
                text_c = c.get("text") or str(c)
                color = (255, 255, 0) if i == choice_idx else (255, 255, 255)
                surf = self.font.render(text_c, True, color)
                surface.blit(surf, (self.choice_pos[0], self.choice_pos[1] + i * 40))
        
        # Draw speaker and text
        elif text:
            # Check if new text to display
            if text != self.current_full_text:
                self.current_full_text = text
                self.visible_chars = 0.0
                self.text_timer = 0.0
                self.is_typing = True
            
            # Show speaker name if provided
            if speaker and self.speaker_font:
                spk_surf = self.speaker_font.render(f"{speaker}:", True, (255, 255, 0))
                surface.blit(spk_surf, self.speaker_pos)
            
            # Draw text with typing effect
            if self.font:
                visible_text = self.current_full_text[0 : int(self.visible_chars)]
                
                txt_surf = self.font.render(visible_text, True, (255, 255, 255))
                surface.blit(txt_surf, self.text_pos)

    def skip_typing(self):
        self.visible_chars = len(self.current_full_text)
        self.is_typing = False

    def is_finished(self):
        return not self.is_typing

class BattleHUD:
    def __init__(self, engine):
        self.engine = engine

        # Load fonts
        font_path = os.path.join("assets", "fonts", "press-start.k.ttf")
        font_path = font_path if os.path.exists(font_path) else None
        self.font = self.engine.load_font(font_path, 28)
        self.hp_font = self.engine.load_font(font_path, 20)
        
        # Load stats panel image
        self.img_stats_panel = self.engine.load_image("assets/ui/panel_stats.png")
        if self.img_stats_panel:
            self.pos_stats_panel = (400, 400)
        else:
            self.pos_stats_panel = None

    def draw(self, surface, player_hp, enemies, skills, selected_skill_idx):
        
        # Draw stats panel
        if self.img_stats_panel:
            surface.blit(self.img_stats_panel, self.pos_stats_panel)
        # Draw HP and skills
        surface.blit(self.hp_font.render(f"Player HP: {player_hp}", True, (255, 255, 255)), (50, 50))
        
        # Menu positions
        base_x = self.pos_stats_panel[0] + 40 if self.pos_stats_panel else 50
        base_y = self.pos_stats_panel[1] + 50 if self.pos_stats_panel else surface.get_height() - 200
        
        for i, skill in enumerate(skills):
            text = skill.get("text")
            color = (255, 255, 0) if i == selected_skill_idx else (255, 255, 255)
            lbl = self.font.render(text, True, color)
            surface.blit(lbl, (base_x, base_y + i * 40)) 
class ChapterTitle:
    def __init__(self, engine, text, duration=1.5):
        self.engine = engine
        self.text = text
        self.timer = duration # 1.5 seconds
        
        font_path = os.path.join("assets", "fonts", "press-start.k.ttf")
        font_path = font_path if os.path.exists(font_path) else None
        self.font = self.engine.load_font(font_path, 50)
        
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
            # Draw fade effect
            s = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
            alpha = min(200, (self.timer / 1.5) * 200) # Fade out
            s.fill((0, 0, 0, alpha))
            surface.blit(s, (0, 0))
            
            # Draw text
            surface.blit(self.text_surf, self.pos)

            # Draw surface on top
            
    def is_finished(self):
        return self.timer <= 0