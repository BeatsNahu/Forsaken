# Description: Main menu scene for the game
import pygame,sys
import os
from scene import Scene

class MainMenu(Scene):
    def __init__(self, engine): # Initialize the scene with a reference to the engine
        super().__init__(engine, {"id":"menu"}) # Call the parent constructor with the engine and scene data
        self.options = [
<<<<<<< HEAD
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1")},
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)}
=======
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)},
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1_intro")}
>>>>>>> fb203c9 (Merge remote-tracking branch 'origin/main' into Antonio)
        ]
        # Preload fonts via engine cache to avoid recreating them every frame
        font_path = "assets/fonts/press-start.k.ttf"
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

        # Image Options
        self._img_title = None
        self._img_start = None
        self._img_exit = None

    def enter(self): # Called when the scene is entered
        try: # Try to load the background image
            self.bg = pygame.image.load("assets/backgrounds/Menu_v.1.0.png").convert() # Load the background image
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size()) # Scale the image to fit the screen
            
            # Load option images
            self._img_title = pygame.image.load("assets/button/Title.png").convert_alpha() # Load the title image
            self._img_title = pygame.transform.scale(self._img_title,self.engine.screen.get_size()) # Scale the title image to fit the screen
            
            self._img_start = pygame.image.load("assets/button/Start.png").convert_alpha() # Load the start button image
            self._img_start = pygame.transform.scale(self._img_start, (512,512)) # Scale the start button image
            
            self._img_exit = pygame.image.load("assets/button/Exit.png").convert_alpha() # Load the exit button image
            self._img_exit = pygame.transform.scale(self._img_exit, (512,512)) # Scale the exit button image
        
        except Exception: # If there is an error loading the image
            self.bg = None # Set background to None
            self._img_title = None
            self._img_start = None
            self._img_exit = None

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

        if self._img_start and self._img_exit:
            surface.blit(self._img_start, (700, 300))
            surface.blit(self._img_exit, (700, 500))
            if False:
                color = (255,255,0)
                label = self.font.render(opt["text"], True, color) # Render the option text
                surface.blit(label, (740, 450 + 60)) # Draw the option
        
        if self._img_title:
            surface.blit(self._img_title, (0,0))
        else:
            title_font = self.engine.load_font(self._font_path, 100)
            title_label = title_font.render(self.title, True, (255, 255, 255))
            surface.blit(title_label, (800, 200))
        pass
    
SCENE_CLASS = MainMenu





