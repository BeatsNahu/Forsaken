<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# Description: Main menu scene for the game
import pygame
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
# src/scenes/main_menu.py
=======
# Description: Main menu scene for the game
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
=======
# Description: Main menu scene for the game
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
=======
# Description: Main menu scene for the game
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
=======
# Description: Main menu scene for the game
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
=======
# Description: Main menu scene for the game
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
import pygame,sys
import os
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
# src/scenes/main_menu.py
<<<<<<< HEAD
import pygame
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
import pygame,sys
>>>>>>> 59da024 (Finish the window menu, we need to can select one option and swap the scene or exit the game)
=======
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
# src/scenes/main_menu.py
<<<<<<< HEAD
import pygame
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
import pygame,sys
>>>>>>> 59da024 (Finish the window menu, we need to can select one option and swap the scene or exit the game)
=======
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
# src/scenes/main_menu.py
<<<<<<< HEAD
import pygame
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
import pygame,sys
>>>>>>> 59da024 (Finish the window menu, we need to can select one option and swap the scene or exit the game)
=======
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
# src/scenes/main_menu.py
<<<<<<< HEAD
import pygame
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
import pygame,sys
>>>>>>> 59da024 (Finish the window menu, we need to can select one option and swap the scene or exit the game)
=======
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
from scene import Scene

class MainMenu(Scene):
    def __init__(self, engine): # Initialize the scene with a reference to the engine
        super().__init__(engine, {"id":"menu"}) # Call the parent constructor with the engine and scene data
        self.options = [
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1")},
=======
=======
>>>>>>> af4af9d (Create def draw in the scene file to load data driven)
=======
>>>>>>> 049ad1e (feat: implement buttons and characters)
=======
>>>>>>> c98b9a9 (Merge remote-tracking branch 'origin/main' into Antonio)
=======
>>>>>>> 1e72137 (fix: update scene backgrounds and titles for consistency across chapters)
=======
=======
>>>>>>> 83239ec (feat: add battle scene structure and dialogue for new encounters)
>>>>>>> 4b44c82 (feat: add battle scene structure and dialogue for new encounters)
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1_intro")},
>>>>>>> c3173b0 (fix: update scene backgrounds and titles for consistency across chapters)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1_intro")},
>>>>>>> 83239ec (feat: add battle scene structure and dialogue for new encounters)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1_intro")},
>>>>>>> 83239ec (feat: add battle scene structure and dialogue for new encounters)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1_intro")},
>>>>>>> 83239ec (feat: add battle scene structure and dialogue for new encounters)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1_intro")},
>>>>>>> 83239ec (feat: add battle scene structure and dialogue for new encounters)
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)}
=======
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)},
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1_intro")}
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fb203c9 (Merge remote-tracking branch 'origin/main' into Antonio)
=======
>>>>>>> fb203c9 (Merge remote-tracking branch 'origin/main' into Antonio)
=======
>>>>>>> fb203c9 (Merge remote-tracking branch 'origin/main' into Antonio)
=======
>>>>>>> fb203c9 (Merge remote-tracking branch 'origin/main' into Antonio)
=======
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
<<<<<<< HEAD
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch0")}
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1")}
>>>>>>> c79f79d (canvio en que main vaya a chapter 1 en vez de a chapter 0)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1")},
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1_intro")},
>>>>>>> c3173b0 (fix: update scene backgrounds and titles for consistency across chapters)
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)}
>>>>>>> a9e0d67 (feat: implement buttons and characters)
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
<<<<<<< HEAD

        # Used images 
        self.bg = None # Background image
<<<<<<< HEAD
        self._img_title = None
        self._img_start = None
        self._img_exit = None
=======
        self.title = "Forsaken" # Title text
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)

        # Used images 
        self.bg = None # Background image
        self._img_title = None
        self._img_start = None
        self._img_exit = None
<<<<<<< HEAD
        # store scaled rects for layout
        self._title_rect = None
        self._option_rects = []
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)

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
<<<<<<< HEAD
            self._img_title = None
            self._img_start = None
            self._img_exit = None
=======
        # Load button/title images (fallback to None if not found)
        btn_dir = os.path.join("assets", "button")
        try:
            tpath = os.path.join(btn_dir, "Titulo.png")
            if os.path.exists(tpath):
                self._img_title = pygame.image.load(tpath).convert_alpha()
            spath = os.path.join(btn_dir, "Start.png")
            if os.path.exists(spath):
                self._img_start = pygame.image.load(spath).convert_alpha()
            epath = os.path.join(btn_dir, "Exit.png")
            if os.path.exists(epath):
                self._img_exit = pygame.image.load(epath).convert_alpha()
        except Exception:
            # leave images as None to trigger text fallback
            self._img_title = self._img_start = self._img_exit = None

        # Prepare rects: center title at top, options centered vertically lower
        w, h = self.engine.screen.get_size()
        # Title rect
        if self._img_title:
            self._title_rect = self._img_title.get_rect()
            self._title_rect.centerx = w // 2
            self._title_rect.y = 40
        else:
            self._title_rect = None

        # Option rects (Start, Exit) stacked
        self._option_rects = []
        option_imgs = [self._img_exit, self._img_start]
        # layout start y a bit above center
        base_y = h // 2
        gap = 20
        for i, img in enumerate(option_imgs):
            if img:
                r = img.get_rect()
                r.centerx = w // 2
                r.y = base_y + i * (r.height + gap)
            else:
                # estimate rect based on font size
                label = self.font.render(self.options[i]["text"], True, (255,255,255))
                r = label.get_rect()
                r.centerx = w // 2
                r.y = base_y + i * (r.height + gap)
            self._option_rects.append(r)
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)
=======

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
>>>>>>> a9e0d67 (feat: implement buttons and characters)

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
<<<<<<< HEAD
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
=======
        # Draw title image or fallback text
        if self._img_title and self._title_rect:
            surface.blit(self._img_title, self._title_rect)
        else:
            # fallback to rendered text title
            if not self.title_font:
                try:
                    self.title_font = self.engine.load_font(self._font_path, 125)
                except Exception:
                    self.title_font = pygame.font.Font(self._font_path if os.path.exists(self._font_path) else None, 125)
            title_surf = self.title_font.render(self.title, True, (255,255,255))
            tr = title_surf.get_rect()
            tr.centerx = surface.get_width() // 2
            tr.y = 40
            surface.blit(title_surf, tr)

        # Draw options as images (Exit, Start) with selection highlight
        option_images = [self._img_exit, self._img_start]
        for i, opt in enumerate(self.options):
            img = option_images[i]
            rect = None
            if i < len(self._option_rects):
                rect = self._option_rects[i]
            if img and rect:
                surface.blit(img, rect)
            else:
                # fallback to text rendering centered
                color = (255,255,0) if i == self.selection else (255,255,255)
                label = self.font.render(opt["text"], True, color)
                lr = label.get_rect()
                lr.centerx = surface.get_width() // 2
                # place where rect would be if available
                lr.y = (self._option_rects[i].y if i < len(self._option_rects) else surface.get_height()//2 + i*60)
                surface.blit(label, lr)

            # draw selection indicator (rect outline) around currently selected option
            if rect is None:
                # compute a rect around label for highlight
                sel_rect = pygame.Rect(lr.x - 10, lr.y - 5, lr.width + 20, lr.height + 10)
            else:
                sel_rect = rect.inflate(10, 10)
            if i == self.selection:
                pygame.draw.rect(surface, (255, 215, 0), sel_rect, 4)
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)
        if self.title: # If there is a title
            # use cached title font from engine if available, else create once on demand
            # If self.title_font exists but is None (inherited from Scene), treat it as missing.
            if not self.title_font:
                try:
                    self.title_font = self.engine.load_font(self._font_path, 125)
                except Exception:
                    self.title_font = pygame.font.Font(self._font_path if os.path.exists(self._font_path) else None, 125)
<<<<<<< HEAD
            title_surf = self.title_font.render(self.title, True, (255,255,255)) # Render the title text
            surface.blit(title_surf, (465, 120)) # Draw the title        
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
            # existing text-based title handled above as fallback
            pass
>>>>>>> f0f2483 (feat: enhance battle manager and main menu with image support and improved layout)
=======

        if self._img_start and self._img_exit:
            if self.selection == 0:
                surface.blit(self._img_start_selected, (700, 300))
                surface.blit(self._img_exit, (700, 500))
            else:
                surface.blit(self._img_start, (700, 300))
                surface.blit(self._img_exit_selected, (700, 500))


        if self._img_title:
            surface.blit(self._img_title, (0,0))
<<<<<<< HEAD
        else:
            title_font = self.engine.load_font(self._font_path, 100)
            title_label = title_font.render(self.title, True, (255, 255, 255))
            surface.blit(title_label, (800, 200))
        pass
>>>>>>> a9e0d67 (feat: implement buttons and characters)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
    
SCENE_CLASS = MainMenu
=======
            {"text":"Exit", "action": lambda: setattr(engine, "quit_flag", True)}, # Exit action
            {"text":"Start Game", "action": lambda: engine.scene_manager.load_scene("scripts.ch0")} # Start game action
=======
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)},
<<<<<<< HEAD
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch0")}
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1")}
>>>>>>> c79f79d (canvio en que main vaya a chapter 1 en vez de a chapter 0)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1")},
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1_intro")},
>>>>>>> c3173b0 (fix: update scene backgrounds and titles for consistency across chapters)
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)}
>>>>>>> a9e0d67 (feat: implement buttons and characters)
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

        if self._img_start and self._img_exit:
            if self.selection == 0:
                surface.blit(self._img_start_selected, (700, 300))
                surface.blit(self._img_exit, (700, 500))
            else:
                surface.blit(self._img_start, (700, 300))
                surface.blit(self._img_exit_selected, (700, 500))


        if self._img_title:
            surface.blit(self._img_title, (0,0))
    
<<<<<<< HEAD
=======
            {"text":"Exit", "action": lambda: setattr(engine, "quit_flag", True)}, # Exit action
            {"text":"Start Game", "action": lambda: engine.scene_manager.load_scene("scripts.ch0")} # Start game action
=======
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)},
<<<<<<< HEAD
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch0")}
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1")}
>>>>>>> c79f79d (canvio en que main vaya a chapter 1 en vez de a chapter 0)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1")},
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1_intro")},
>>>>>>> c3173b0 (fix: update scene backgrounds and titles for consistency across chapters)
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)}
>>>>>>> a9e0d67 (feat: implement buttons and characters)
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
<<<<<<< HEAD
=======
            {"text":"Exit", "action": lambda: setattr(engine, "quit_flag", True)}, # Exit action
            {"text":"Start Game", "action": lambda: engine.scene_manager.load_scene("scripts.ch0")} # Start game action
=======
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)},
<<<<<<< HEAD
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch0")}
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1")}
>>>>>>> c79f79d (canvio en que main vaya a chapter 1 en vez de a chapter 0)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1")},
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1_intro")},
>>>>>>> c3173b0 (fix: update scene backgrounds and titles for consistency across chapters)
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)}
>>>>>>> a9e0d67 (feat: implement buttons and characters)
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
<<<<<<< HEAD
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
            {"text":"Exit", "action": lambda: setattr(engine, "quit_flag", True)}, # Exit action
            {"text":"Start Game", "action": lambda: engine.scene_manager.load_scene("scripts.ch0")} # Start game action
=======
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)},
<<<<<<< HEAD
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch0")}
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1")}
>>>>>>> c79f79d (canvio en que main vaya a chapter 1 en vez de a chapter 0)
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1")},
=======
            {"text": "Start Game", "action": lambda: self.engine.scene_manager.load_scene("scripts.ch1_intro")},
>>>>>>> c3173b0 (fix: update scene backgrounds and titles for consistency across chapters)
            {"text": "Exit", "action": lambda: setattr(self.engine, "quit_flag", True)}
>>>>>>> a9e0d67 (feat: implement buttons and characters)
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

        # Used images 
        self.bg = None # Background image
        self._img_title = None
        self._img_start = None
        self._img_exit = None

    def enter(self): # Called when the scene is entered
        try:
    # Usamos self.engine.load_image()
            self.bg = self.engine.load_image("assets/backgrounds/Menu_scenary.png")
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size()) 
    
            self._img_title = self.engine.load_image("assets/button/Title.png")
            self._img_title = pygame.transform.scale(self._img_title, self.engine.screen.get_size())
    
            self._img_start = self.engine.load_image("assets/button/Start.png")
            self._img_start = pygame.transform.scale(self._img_start, (512,512))
    
            self._img_exit = self.engine.load_image("assets/button/Exit.png")
            self._img_exit = pygame.transform.scale(self._img_exit, (512,512))
        
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
<<<<<<< HEAD
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
            surface.blit(self.bg, (0,0))
        font = pygame.font.SysFont(None, 48)
        for i, opt in enumerate(self.options):
            color = (255,255,0) if i == self.sel else (255,255,255)
            label = font.render(opt["text"], True, color)
            surface.blit(label, (100, 200 + i*60))

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
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
    
<<<<<<< HEAD
>>>>>>> 59da024 (Finish the window menu, we need to can select one option and swap the scene or exit the game)
=======
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
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
    
<<<<<<< HEAD
>>>>>>> 59da024 (Finish the window menu, we need to can select one option and swap the scene or exit the game)
=======
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
            surface.blit(self.bg, (0,0)) # Draw the background image

        if self._img_start and self._img_exit:
            surface.blit(self._img_start, (700, 300))
            surface.blit(self._img_exit, (700, 500))

        if self._img_title:
            surface.blit(self._img_title, (0,0))
    
<<<<<<< HEAD
>>>>>>> 59da024 (Finish the window menu, we need to can select one option and swap the scene or exit the game)
SCENE_CLASS = MainMenu





<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
SCENE_CLASS = MainMenu
>>>>>>> 6044657 (refactor: clean up comments and improve enemy initialization in BattleManager)
=======
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
SCENE_CLASS = MainMenu
>>>>>>> 6044657 (refactor: clean up comments and improve enemy initialization in BattleManager)
=======
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
SCENE_CLASS = MainMenu
>>>>>>> 6044657 (refactor: clean up comments and improve enemy initialization in BattleManager)
=======
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
SCENE_CLASS = MainMenu
>>>>>>> 6044657 (refactor: clean up comments and improve enemy initialization in BattleManager)
