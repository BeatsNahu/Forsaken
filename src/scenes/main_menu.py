# Description: Main menu scene for the game
import pygame
import os
import config
from core.scene import Scene

class MainMenu(Scene):
    def __init__(self, engine): # Initialize the scene with a reference to the engine
        super().__init__(engine, {"id":"menu"}) # Call the parent constructor with the engine and scene data
        self.options = [
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scenes.ch5_knife_fight")},
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)}
        ]
        # body font (used 
        try:
            self.font = self.engine.load_font(config.FONT_PATH_DEFAULT, config.FONT_SIZE_MENU)
        except Exception as e:
            print(f"Error al cargar fuente de menú (fallback): {e}")
            self.font = pygame.font.Font(None, config.FONT_SIZE_MENU)

        self.selection = 0 # Selected option index

        # Used images 
        self.bg = None # Background image
        self._img_title = None
        self._img_start = None
        self._img_exit = None

    def enter(self): # Called when the scene is entered
        super().enter()

        # Sounds
        self.engine.play_music("assets/audio/music/main_track.ogg", loop=-1, volume=0.1) # Background music

        try:
    # Usamos self.engine.load_image()
            self.bg = self.engine.load_image("assets/backgrounds/menu_scenery.png")
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size()) 
    
            self._img_title = self.engine.load_image("assets/ui/title.png")
            self._img_title = pygame.transform.scale(self._img_title, self.engine.screen.get_size())
    
            self._img_start = self.engine.load_image("assets/ui/buttons/start.png")
            self._img_start = pygame.transform.scale(self._img_start, (512,512))

            self._img_start_selected = self.engine.load_image("assets/ui/buttons/start_selected.png")
            self._img_start_selected = pygame.transform.scale(self._img_start_selected, (512,512))
    
            self._img_exit = self.engine.load_image("assets/ui/buttons/exit.png")
            self._img_exit = pygame.transform.scale(self._img_exit, (512,512))

            self._img_exit_selected = self.engine.load_image("assets/ui/buttons/exit_selected.png")
            self._img_exit_selected = pygame.transform.scale(self._img_exit_selected, (512,512))
        
        except Exception: # If there is an error loading the image
            self.bg = None # Set background to None
            self._img_title = None
            self._img_start = None
            self._img_exit = None

    def handle_event(self, event): # Handle events
        if event.type == pygame.KEYDOWN: # If a key is pressed
            if event.key == pygame.K_ESCAPE:
                setattr(self.engine, "quit_flag", True)
            elif event.key == pygame.K_DOWN: # If the down arrow key is pressed
                self.selection = (self.selection + 1) % len(self.options) # Move selection down, wrapping around
                self.engine.play_sound(config.SFX_UI_SWAP, volume=0.05) # Play option select sound
            elif event.key == pygame.K_UP: # If the up arrow key is pressed
                self.selection = (self.selection - 1) % len(self.options) # Move selection up, wrapping around
                self.engine.play_sound(config.SFX_UI_SWAP, volume=0.05) # Play option select sound
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER): # If the enter key is pressed
                self.options[self.selection]["action"]() # Execute the action of the selected option
                self.engine.play_sound(config.SFX_UI_CONFIRM, volume=0.05) # Play option select sound

    def draw(self, surface):
        if self.bg:
            surface.blit(self.bg, (0,0)) # Draw the background image

        if self._img_start and self._img_exit:
            if self.selection == 0:
                surface.blit(self._img_start_selected, (700, 300))
                surface.blit(self._img_exit, (700, 500))
            else:
                surface.blit(self._img_start, (700, 300))
                surface.blit(self._img_exit_selected, (700, 500))


        if self._img_title:
            surface.blit(self._img_title, (0,0))
    
SCENE_CLASS = MainMenu