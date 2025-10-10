# src/scenes/main_menu.py
import pygame
from scene import Scene

class MainMenu(Scene):
    def __init__(self, engine): # Initialize the scene with a reference to the engine
        super().__init__(engine, {"id":"menu"}) # Call the parent constructor with the engine and scene data
        self.options = [
            {"text":"Exit", "action": lambda: setattr(engine, "quit_flag", True)}, # Exit action
            {"text":"Start Game", "action": lambda: engine.scene_manager.load_scene("scripts.gameplay")} # Start game action
        ]
        self.sel = 0 # Selected option index
        self.bg = None # Background image

    def enter(self): # Called when the scene is entered
        try: # Try to load the background image
            self.bg = pygame.image.load("assets/backgrounds/prueba_menu.jpg") # Load the background image
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size()) # Scale the image to fit the screen
        except Exception: # If there is an error loading the image
            self.bg = None # Set background to None

    def handle_event(self, event): # Handle events
        if event.type == pygame.KEYDOWN: # If a key is pressed
            if event.key == pygame.K_DOWN: # If the down arrow key is pressed
                self.sel = (self.sel + 1) % len(self.options) # Move selection down, wrapping around
            elif event.key == pygame.K_UP: # If the up arrow key is pressed
                self.sel = (self.sel - 1) % len(self.options) # Move selection up, wrapping around
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER): # If the enter key is pressed
                self.options[self.sel]["action"]() # Execute the action of the selected option

    def draw(self, surface):
        if self.bg:
            surface.blit(self.bg, (0,0))
        font = pygame.font.SysFont(None, 48)
        for i, opt in enumerate(self.options):
            color = (255,255,0) if i == self.sel else (255,255,255)
            label = font.render(opt["text"], True, color)
            surface.blit(label, (100, 200 + i*60))

SCENE_CLASS = MainMenu





