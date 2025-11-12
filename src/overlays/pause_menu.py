import pygame
import config
from overlays.inventory_menu import InventoryMenu

class PauseMenu:
    def __init__(self, engine):
        self.engine = engine
        self.options = [
            {"text": "Continuar", "action": "POP"},
            {"text": "Inventario", "action": "INVENTORY"},
            {"text": "Salir al Menú", "action": "LOAD_SCENE"},
            {"text": "Salir del Juego", "action": "QUIT"}
        ]
        self.selection = 0
        
        self.font = self.engine.load_font(config.FONT_PATH_DEFAULT, config.FONT_SIZE_MENU)
        self.sfx_swap = config.SFX_UI_SWAP
        self.sfx_confirm = config.SFX_UI_CONFIRM


        self.veil = pygame.Surface(self.engine.screen.get_size(), pygame.SRCALPHA)
        self.veil.fill((0, 0, 0, 180))
        
    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_ESCAPE:
            self.engine.pop_overlay()
            
        elif event.key == pygame.K_DOWN:
            self.selection = (self.selection + 1) % len(self.options)
            self.engine.play_sound(self.sfx_swap, volume=0.5)
            
        elif event.key == pygame.K_UP:
            self.selection = (self.selection - 1) % len(self.options)
            self.engine.play_sound(self.sfx_swap, volume=0.5)
            
        elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
            self.engine.play_sound(self.sfx_confirm, volume=0.5)
            selected_action = self.options[self.selection]["action"]
            
            if selected_action == "POP":
                self.engine.pop_overlay()
            elif selected_action == "INVENTORY":
                self.engine.push_overlay(InventoryMenu(self.engine))
            elif selected_action == "LOAD_SCENE":
                self.engine.pop_overlay()
                self.engine.scene_manager.load_scene("scenes.main_menu")
            elif selected_action == "QUIT":
                setattr(self.engine, "quit_flag", True)

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.blit(self.veil, (0, 0))
        
        color_selected = config.COLOR_YELLOW
        color_default = config.COLOR_WHITE
        
        screen_center_x = self.engine.screen.get_width() // 2
        start_y = 400
        
        for i, option in enumerate(self.options):
            text = option["text"]
            color = color_selected if i == self.selection else color_default
            
            text_surf = self.font.render(text, True, color)
            text_rect = text_surf.get_rect(center=(screen_center_x, start_y + i * 80))
            surface.blit(text_surf, text_rect)