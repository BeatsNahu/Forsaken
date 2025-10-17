# src/scenes/main_menu.py
import pygame,sys
from scene import Scene

class MainMenu(Scene):
    def __init__(self, engine): # Initialize the scene with a reference to the engine
        super().__init__(engine, {"id":"menu"}) # Call the parent constructor with the engine and scene data
        self.options = [
            {"text":"Exit", "action": lambda: setattr(engine, "quit_flag", True)}, # Exit action
            {"text":"Start Game", "action": lambda: engine.scene_manager.load_scene("scripts.ch0")} # Start game action
        ]
        self.font = pygame.font.Font("assets/fonts/press-start.k.ttf", 50) # Load the font
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
            title_font = pygame.font.Font("assets/fonts/press-start.k.ttf", 125) # Load a larger font for the title
            title_surf = title_font.render(self.title, True, (255,255,255)) # Render the title text
            surface.blit(title_surf, (465, 120)) # Draw the title        
    
SCENE_CLASS = MainMenu





