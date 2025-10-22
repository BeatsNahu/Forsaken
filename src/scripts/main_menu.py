# src/scenes/main_menu.py
import pygame,sys
import os
from scene import Scene

class MainMenu(Scene):
    def __init__(self, engine): # Initialize the scene with a reference to the engine
        super().__init__(engine, {"id":"menu"}) # Call the parent constructor with the engine and scene data
        self.options = [
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)},
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1")}
        ]
        # Preload fonts via engine cache to avoid recreating them every frame
        font_path = os.path.join("assets", "fonts", "press-start.k.ttf")
        # keep path on self so other methods (draw) can reference it
        self._font_path = font_path
        # body font (used for menu options)
        try:
            self.font = self.engine.load_font(self._font_path, 50)
        except Exception:
            # fallback: create directly
            self.font = pygame.font.Font(self._font_path if os.path.exists(self._font_path) else None, 50)
        self.selection = 0 # Selected option index
        self.bg = None # Background image
        self.title = "Forsaken" # Title text

    def enter(self): # Called when the scene is entered
        try: # Try to load the background image
            self.bg = pygame.image.load("assets/backgrounds/Menu_v.1.0.png").convert() # Load the background image
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size()) # Scale the image to fit the screen
        except Exception: # If there is an error loading the image
            self.bg = None # Set background to None

    def handle_event(self, event): # Handle events
        if event.type == pygame.KEYDOWN: # If a key is pressed
            if event.key == pygame.K_ESCAPE: # If the escape key is pressed
                pygame.quit() # Quit pygame
                sys.exit() # Exit the program
            elif event.key == pygame.K_DOWN: # If the down arrow key is pressed
                self.selection = (self.selection + 1) % len(self.options) # Move selection down, wrapping around                
            elif event.key == pygame.K_UP: # If the up arrow key is pressed
                self.selection = (self.selection - 1) % len(self.options) # Move selection up, wrapping around
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER): # If the enter key is pressed
                self.options[self.selection]["action"]() # Execute the action of the selected option

    def draw(self, surface):
        if self.bg:
            surface.blit(self.bg, (0,0)) # Draw the background image
        for i, opt in enumerate(self.options): # Draw each menu option
            color = (255,255,0) if i == self.selection else (255,255,255) # Highlight the selected option
            label = self.font.render(opt["text"], True, color) # Render the option text
            surface.blit(label, (740, 450 + i*60)) # Draw the option
        if self.title: # If there is a title
            # use cached title font from engine if available, else create once on demand
            # If self.title_font exists but is None (inherited from Scene), treat it as missing.
            if not self.title_font:
                try:
                    self.title_font = self.engine.load_font(self._font_path, 125)
                except Exception:
                    self.title_font = pygame.font.Font(self._font_path if os.path.exists(self._font_path) else None, 125)
            title_surf = self.title_font.render(self.title, True, (255,255,255)) # Render the title text
            surface.blit(title_surf, (465, 120)) # Draw the title        
    
SCENE_CLASS = MainMenu





