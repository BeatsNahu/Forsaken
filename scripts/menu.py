# src/scenes/main_menu.py
import pygame
from scene import Scene

class MainMenu(Scene):
    def __init__(self, engine):
        super().__init__(engine, {"id":"menu"})
        self.options = [
            {"text":"Salir", "action": lambda: setattr(engine, "quit_flag", True)}
        ]
        self.sel = 0
        self.bg = None

    def enter(self):
        # cargar fondo - usar engine.assets si existe
        try:
            self.bg = pygame.image.load("assets/backgrounds/prueba_menu.jpg")
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size())
        except Exception:
            self.bg = None

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.sel = (self.sel + 1) % len(self.options)
            elif event.key == pygame.K_UP:
                self.sel = (self.sel - 1) % len(self.options)
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self.options[self.sel]["action"]()

    def draw(self, surface):
        if self.bg:
            surface.blit(self.bg, (0,0))
        font = pygame.font.SysFont(None, 48)
        for i, opt in enumerate(self.options):
            color = (255,255,0) if i == self.sel else (255,255,255)
            label = font.render(opt["text"], True, color)
            surface.blit(label, (100, 200 + i*60))

SCENE_CLASS = MainMenu





