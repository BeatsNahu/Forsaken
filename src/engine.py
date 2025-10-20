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

    def load_font(self, path, size):
        """Load and cache pygame Font instances.

        Returns a pygame.font.Font for the given path and size. If the
        file does not exist, falls back to the default pygame font.
        Cached by (path, size) to avoid reloading every frame.
        """
        key = (path, size)
        if key in self._font_cache:
            return self._font_cache[key]

        try:
            if path and os.path.exists(path):
                f = pygame.font.Font(path, size)
            else:
                f = pygame.font.Font(None, size)
        except Exception:
            # On any failure, fallback to default font
            f = pygame.font.Font(None, size)

        self._font_cache[key] = f
        return f
    