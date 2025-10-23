import pygame
import os


class Engine:
    def __init__(self): # Constructor of the class
        self.name = None # Name of the engine
        self.scene_manager = None # Scene manager of the engine
        self.screen = None # Screen of the engine
        self.clock = None # Clock of the engine
        self.quit_flag = False # Flag to indicate if the game should quit
        self.state = {}
        # simple resource caches
        self._font_cache = {}

    def load_font(self, path, size): # Load a font from a given path and size
        key = (path, size) # Create a key for the font cache based on path and size
        if key in self._font_cache: # If the font is already in the cache, return it
            return self._font_cache[key] # Return the cached font

        try:
            if path and os.path.exists(path): # If the path is valid and the file exists, load the font from the given path
                f = pygame.font.Font(path, size) # Load the font from the given path
            else:
                f = pygame.font.Font(None, size) # Load the default font
        except Exception:
            # On any failure, fallback to default font
            f = pygame.font.Font(None, size) # Load the default font

        self._font_cache[key] = f # Cache the loaded font
        return f # Return the loaded font
    