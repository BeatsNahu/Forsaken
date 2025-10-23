# Description: Main menu scene for the game
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
        # Image placeholders (will be loaded in enter)
        self._img_title = None
        self._img_start = None
        self._img_exit = None
        # store scaled rects for layout
        self._title_rect = None
        self._option_rects = []

    def enter(self): # Called when the scene is entered
        try: # Try to load the background image
            self.bg = pygame.image.load("assets/backgrounds/Menu_v.1.0.png").convert() # Load the background image
            self.bg = pygame.transform.scale(self.bg, self.engine.screen.get_size()) # Scale the image to fit the screen
        except Exception: # If there is an error loading the image
            self.bg = None # Set background to None
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
        if self.title: # If there is a title
            # use cached title font from engine if available, else create once on demand
            # If self.title_font exists but is None (inherited from Scene), treat it as missing.
            if not self.title_font:
                try:
                    self.title_font = self.engine.load_font(self._font_path, 125)
                except Exception:
                    self.title_font = pygame.font.Font(self._font_path if os.path.exists(self._font_path) else None, 125)
            # existing text-based title handled above as fallback
            pass
    
SCENE_CLASS = MainMenu





