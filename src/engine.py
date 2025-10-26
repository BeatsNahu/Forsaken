import pygame
import os
from transition_manager import TransitionManager

class Engine:
    def __init__(self): # Constructor of the class
        self.name = None # Name of the engine
        self.scene_manager = None # Scene manager of the engine
        self.screen = None # Screen of the engine
        self.clock = None # Clock of the engine
        self.quit_flag = False # Flag to indicate if the game should quit
        self.state = {
            "inventory": [],
            "game_vars": {}
        } 
        # TransitionManager requires engine.screen to be available.
        # We delay its creation until the screen is assigned by the caller (see main.py).
        self.transition_manager = None

        # simple resource caches
        self._font_cache = {}
        self._image_cache = {}
        self._sound_cache = {}

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

    def load_image(self, path):
        """Carga una imagen desde un path, la cachea y la devuelve."""
        if path in self._image_cache:
            return self._image_cache[path] # Devuelve la copia en memoria

        if not path or not os.path.exists(path):
            print(f"Error: No se encontró la imagen {path}")
            return None 

        try:
            # 1. Cargar la imagen SIN convertirla todavía
            image = pygame.image.load(path)

            # 2. ¡LA CORRECCIÓN!
            # Detectar si la imagen tiene canal alfa (transparencia)
            if image.get_alpha():
                # Si tiene, usar convert_alpha()
                image = image.convert_alpha()
            else:
                # Si no tiene (es opaca, como un JPG), usar convert()
                image = image.convert()
            
            # 3. Guardar la imagen correctamente convertida en el caché
            self._image_cache[path] = image
            return image
            
        except Exception as e:
            print(f"Error al cargar imagen {path}: {e}")
            return None
        
    def play_sound(self, path):
        """Carga un sonido, lo cachea y lo reproduce."""
        if path not in self._sound_cache:
            if not path or not os.path.exists(path):
                print(f"Error: No se encontró el sonido {path}")
                return
            try:
                # Carga del disco
                self._sound_cache[path] = pygame.mixer.Sound(path)
            except Exception as e:
                print(f"Error al cargar sonido {path}: {e}")
                return
        
        # Reproduce el sonido cacheado
        self._sound_cache[path].play()

    def add_item(self, item_id):
        """Añade un item al inventario global."""
        if item_id and item_id not in self.state["inventory"]:
            self.state["inventory"].append(item_id)
            print(f"[Engine] Item añadido: {item_id}")

    def set_var(self, var_name, value):
        """Establece una variable de estado global."""
        if var_name:
            self.state["game_vars"][var_name] = value
            print(f"[Engine] Variable: {var_name} = {value}")
    
    def get_var(self, var_name):
        """Consulta una variable de estado global."""
        return self.state["game_vars"].get(var_name)
    
    def apply_effects(self, effects):
        """Procesa una lista de efectos de datos (de ex_base.py)."""
        if not effects:
            return

        for e in effects:
            if not isinstance(e, dict):
                continue

            t = e.get("type")

            if t == "give_item":
                self.add_item(e.get("item"))
            elif t == "set_var":
                self.set_var(e.get("name"), e.get("value"))
            elif t == "start_battle":
                # El motor es responsable de cargar escenas
                if e.get("battle_module"):
                    self.scene_manager.load_scene(e.get("battle_module"))