<<<<<<< HEAD
# Description: Main menu scene for the game
import pygame
=======
# src/scenes/main_menu.py
import pygame,sys
import os
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
from scene import Scene

class MainMenu(Scene):
    def __init__(self, engine): # Initialize the scene with a reference to the engine
        super().__init__(engine, {"id":"menu"}) # Call the parent constructor with the engine and scene data
        self.options = [
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1")},
=======
=======
>>>>>>> af4af9d (Create def draw in the scene file to load data driven)
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1_intro")},
>>>>>>> c3173b0 (fix: update scene backgrounds and titles for consistency across chapters)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1_intro")},
>>>>>>> 83239ec (feat: add battle scene structure and dialogue for new encounters)
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
            {"text":"Exit", "action": lambda: setattr(engine, "quit_flag", True)}, # Exit action
            {"text":"Start Game", "action": lambda: engine.scene_manager.load_scene("scripts.ch0")} # Start game action
=======
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)},
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch0")}
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
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

        # Used images 
        self.bg = None # Background image
        self._img_title = None
        self._img_start = None
        self._img_exit = None

    def enter(self): # Called when the scene is entered
        super().enter()

        # Sounds
        self.engine.play_music("assets/Sounds/main_track.ogg", loop=-1) # Background music

        try:
    # Usamos self.engine.load_image()
            self.bg = self.engine.load_image("assets/backgrounds/Menu_scenary.png")
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size()) 
    
            self._img_title = self.engine.load_image("assets/button/Title.png")
            self._img_title = pygame.transform.scale(self._img_title, self.engine.screen.get_size())
    
            self._img_start = self.engine.load_image("assets/button/Start.png")
            self._img_start = pygame.transform.scale(self._img_start, (512,512))

            self._img_start_selected = self.engine.load_image("assets/button/Start_selected.png")
            self._img_start_selected = pygame.transform.scale(self._img_start_selected, (512,512))
    
            self._img_exit = self.engine.load_image("assets/button/Exit.png")
            self._img_exit = pygame.transform.scale(self._img_exit, (512,512))

            self._img_exit_selected = self.engine.load_image("assets/button/Exit_selected.png")
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
            elif event.key == pygame.K_UP: # If the up arrow key is pressed
                self.selection = (self.selection - 1) % len(self.options) # Move selection up, wrapping around
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER): # If the enter key is pressed
                self.options[self.selection]["action"]() # Execute the action of the selected option

    def draw(self, surface):
        if self.bg:
            surface.blit(self.bg, (0,0)) # Draw the background image
<<<<<<< HEAD

        if self._img_start and self._img_exit:
            if self.selection == 0:
                surface.blit(self._img_start_selected, (700, 300))
                surface.blit(self._img_exit, (700, 500))
            else:
                surface.blit(self._img_start, (700, 300))
                surface.blit(self._img_exit_selected, (700, 500))


        if self._img_title:
            surface.blit(self._img_title, (0,0))
=======
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
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
    
SCENE_CLASS = MainMenu