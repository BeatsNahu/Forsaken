<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import pygame
import os
<<<<<<< HEAD
<<<<<<< HEAD
from transition_manager import TransitionManager
=======

>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
from transition_manager import TransitionManager
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
import pygame
import os
<<<<<<< HEAD

>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
from transition_manager import TransitionManager
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
import pygame
import os
<<<<<<< HEAD

>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
from transition_manager import TransitionManager
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
import pygame
import os
<<<<<<< HEAD

>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
from transition_manager import TransitionManager
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
import pygame
import os

>>>>>>> d07fceb (Create def draw in the scene file to load data driven)

class Engine:
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
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
    def __init__(self): # Buiilder of the engine
        self.name = None # Name of the engine
        self.scene_manager = None # Scene manager of the engine
        self.screen = None # Screen of the engine
        self.clock = None # Clock of the engine
        self.quit_flag = False # Flag to indicate if the game should quit
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
        self.state = {
            "inventory": [],
            "game_vars": {}
        } 
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)

        # TransitionManager requires engine.screen to be available.
        self.transition_manager = None

        # Simple resource caches
        self._font_cache = {}
        self._image_cache = {}
        self._sound_cache = {}

        self._current_music_path = None

    def play_music(self, path, loop=-1, volume=0.7):
        # Play background music from a given path
        if not path:
            return
        
        # Avoid restarting the same music
        if path == self._current_music_path:
            return
            
        try:
            # Stop current music
            pygame.mixer.music.stop()
            
            # Load and play new music
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(loop) # loop=-1 Loop indefinitely
            
            self._current_music_path = path
            print(f"[Engine] Reproduciendo música: {path}")
            
        except Exception as e:
            print(f"Error al reproducir música {path}: {e}")
            self._current_music_path = None

    def stop_music(self):
        pygame.mixer.music.stop()
        self._current_music_path = None

    def fadeout_music(self, duration_ms):
        pygame.mixer.music.fadeout(duration_ms)
        self._current_music_path = None
=======
        # TransitionManager requires engine.screen to be available.
        self.transition_manager = None

        # Simple resource caches
        self._font_cache = {}
        self._image_cache = {}
        self._sound_cache = {}
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)

        self._current_music_path = None

    def play_music(self, path, loop=-1, volume=0.7):
        # Play background music from a given path
        if not path:
            return
        
        # Avoid restarting the same music
        if path == self._current_music_path:
            return
            
        try:
            # Stop current music
            pygame.mixer.music.stop()
            
            # Load and play new music
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(loop) # loop=-1 Loop indefinitely
            
            self._current_music_path = path
            print(f"[Engine] Reproduciendo música: {path}")
            
        except Exception as e:
            print(f"Error al reproducir música {path}: {e}")
            self._current_music_path = None

    def stop_music(self):
        pygame.mixer.music.stop()
        self._current_music_path = None

    def fadeout_music(self, duration_ms):
        pygame.mixer.music.fadeout(duration_ms)
        self._current_music_path = None
=======
        # TransitionManager requires engine.screen to be available.
        self.transition_manager = None

        # Simple resource caches
        self._font_cache = {}
        self._image_cache = {}
        self._sound_cache = {}
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)

        self._current_music_path = None

    def play_music(self, path, loop=-1, volume=0.7):
        # Play background music from a given path
        if not path:
            return
        
        # Avoid restarting the same music
        if path == self._current_music_path:
            return
            
        try:
            # Stop current music
            pygame.mixer.music.stop()
            
            # Load and play new music
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(loop) # loop=-1 Loop indefinitely
            
            self._current_music_path = path
            print(f"[Engine] Reproduciendo música: {path}")
            
        except Exception as e:
            print(f"Error al reproducir música {path}: {e}")
            self._current_music_path = None

    def stop_music(self):
        pygame.mixer.music.stop()
        self._current_music_path = None

    def fadeout_music(self, duration_ms):
        pygame.mixer.music.fadeout(duration_ms)
        self._current_music_path = None
=======
        # TransitionManager requires engine.screen to be available.
        self.transition_manager = None

        # Simple resource caches
        self._font_cache = {}
        self._image_cache = {}
        self._sound_cache = {}
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)

        self._current_music_path = None

    def play_music(self, path, loop=-1, volume=0.7):
        # Play background music from a given path
        if not path:
            return
        
        # Avoid restarting the same music
        if path == self._current_music_path:
            return
            
        try:
            # Stop current music
            pygame.mixer.music.stop()
            
            # Load and play new music
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(loop) # loop=-1 Loop indefinitely
            
            self._current_music_path = path
            print(f"[Engine] Reproduciendo música: {path}")
            
        except Exception as e:
            print(f"Error al reproducir música {path}: {e}")
            self._current_music_path = None

    def stop_music(self):
        pygame.mixer.music.stop()
        self._current_music_path = None

    def fadeout_music(self, duration_ms):
        pygame.mixer.music.fadeout(duration_ms)
        self._current_music_path = None

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if path in self._image_cache:
            return self._image_cache[path] # Return cached image
<<<<<<< HEAD

        if not path or not os.path.exists(path):
            print(f"Error: No se encontró la imagen {path}") # If the path is invalid or the file does not exist, print an error message
            return None 

        try:
            # From disk
            image = pygame.image.load(path)

            # If the image has an alpha channel, convert with alpha (png, gif, etc.)
            if image.get_alpha():
                # Use the alpha channel
                image = image.convert_alpha()
            else:
                # It's a simple image without alpha (jpg, bmp, etc.)
                image = image.convert()
            
            # Cache and return
            self._image_cache[path] = image
            return image
            
        except Exception as e:
            print(f"Error al cargar imagen {path}: {e}") # Print an error message if loading fails
            return None
        
    def play_sound(self, path):
        # Check cache
        if path not in self._sound_cache:
            if not path or not os.path.exists(path):
                print(f"Error: No se encontró el sonido {path}")
                return
            try:
                # Charge from disk
                self._sound_cache[path] = pygame.mixer.Sound(path)
            except Exception as e:
                print(f"Error al cargar sonido {path}: {e}")
                return
        
        # Play sound cached
        self._sound_cache[path].play()

    def add_item(self, item_id):
        # Add an item to the inventory
        if item_id and item_id not in self.state["inventory"]:
            self.state["inventory"].append(item_id)
            print(f"[Engine] Item añadido: {item_id}")

    def set_var(self, var_name, value):
        # Set a global state variable for example, "has_key" = True or "player_health" = 100
        if var_name:
            self.state["game_vars"][var_name] = value
            print(f"[Engine] Variable: {var_name} = {value}")
    
    def get_var(self, var_name):
        # Get a global state variable
        return self.state["game_vars"].get(var_name)
    
    def apply_effects(self, effects):
        # Apply a list of effects to the game state
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
                # The battle module to load is specified in the effect
                if e.get("battle_module"):
                    self.scene_manager.load_scene(e.get("battle_module"))
=======
    def __init__(self, name): # Constructor of the class
        self.name = Forsaken # Name of the engine
=======
    def __init__(self): # Constructor of the class
        self.name = None # Name of the engine
>>>>>>> b4d0ed7 (Run and debug)
        self.scene_manager = None # Scene manager of the engine
        self.screen = None # Screen of the engine
        self.clock = None # Clock of the engine
        self.quit_flag = False # Flag to indicate if the game should quit
>>>>>>> 32ed7b6 (Edition and comments of main.py)
=======
        self.state = {}
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        # TransitionManager requires engine.screen to be available.
        self.transition_manager = None

<<<<<<< HEAD
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
        # simple resource caches
=======
        # Simple resource caches
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
        self._font_cache = {}
        self._image_cache = {}
        self._sound_cache = {}

        self._current_music_path = None

    def play_music(self, path, loop=-1, volume=0.7):
        # Play background music from a given path
        if not path:
            return
        
        # Avoid restarting the same music
        if path == self._current_music_path:
            return
            
        try:
            # Stop current music
            pygame.mixer.music.stop()
            
            # Load and play new music
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(loop) # loop=-1 Loop indefinitely
            
            self._current_music_path = path
            print(f"[Engine] Reproduciendo música: {path}")
            
        except Exception as e:
            print(f"Error al reproducir música {path}: {e}")
            self._current_music_path = None

    def stop_music(self):
        pygame.mixer.music.stop()
        self._current_music_path = None

    def fadeout_music(self, duration_ms):
        pygame.mixer.music.fadeout(duration_ms)
        self._current_music_path = None

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

<<<<<<< HEAD
        self._font_cache[key] = f
        return f
    
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
        self._font_cache[key] = f # Cache the loaded font
        return f # Return the loaded font
<<<<<<< HEAD
    
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
=======

    def load_image(self, path):
        if path in self._image_cache:
            return self._image_cache[path] # Devuelve la copia en memoria
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)

        if not path or not os.path.exists(path):
            print(f"Error: No se encontró la imagen {path}") # If the path is invalid or the file does not exist, print an error message
            return None 

        try:
            # From disk
            image = pygame.image.load(path)

            # If the image has an alpha channel, convert with alpha (png, gif, etc.)
            if image.get_alpha():
                # Use the alpha channel
                image = image.convert_alpha()
            else:
                # It's a simple image without alpha (jpg, bmp, etc.)
                image = image.convert()
            
            # Cache and return
=======
        """Carga una imagen desde un path, la cachea y la devuelve."""
=======
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
        if path in self._image_cache:
            return self._image_cache[path] # Return cached image

        if not path or not os.path.exists(path):
            print(f"Error: No se encontró la imagen {path}") # If the path is invalid or the file does not exist, print an error message
            return None 

        try:
            # From disk
            image = pygame.image.load(path)

            # If the image has an alpha channel, convert with alpha (png, gif, etc.)
            if image.get_alpha():
                # Use the alpha channel
                image = image.convert_alpha()
            else:
                # It's a simple image without alpha (jpg, bmp, etc.)
                image = image.convert()
            
<<<<<<< HEAD
<<<<<<< HEAD
            # 3. Guardar la imagen correctamente convertida en el caché
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
            # 
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
=======
            # Cache and return
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
        """Carga una imagen desde un path, la cachea y la devuelve."""
=======
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
        if path in self._image_cache:
            return self._image_cache[path] # Return cached image

        if not path or not os.path.exists(path):
            print(f"Error: No se encontró la imagen {path}") # If the path is invalid or the file does not exist, print an error message
            return None 

        try:
            # From disk
            image = pygame.image.load(path)

            # If the image has an alpha channel, convert with alpha (png, gif, etc.)
            if image.get_alpha():
                # Use the alpha channel
                image = image.convert_alpha()
            else:
                # It's a simple image without alpha (jpg, bmp, etc.)
                image = image.convert()
            
<<<<<<< HEAD
<<<<<<< HEAD
            # 3. Guardar la imagen correctamente convertida en el caché
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
            # 
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
=======
            # Cache and return
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
        """Carga una imagen desde un path, la cachea y la devuelve."""
=======
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
        if path in self._image_cache:
            return self._image_cache[path] # Return cached image

        if not path or not os.path.exists(path):
            print(f"Error: No se encontró la imagen {path}") # If the path is invalid or the file does not exist, print an error message
            return None 

        try:
            # From disk
            image = pygame.image.load(path)

            # If the image has an alpha channel, convert with alpha (png, gif, etc.)
            if image.get_alpha():
                # Use the alpha channel
                image = image.convert_alpha()
            else:
                # It's a simple image without alpha (jpg, bmp, etc.)
                image = image.convert()
            
<<<<<<< HEAD
<<<<<<< HEAD
            # 3. Guardar la imagen correctamente convertida en el caché
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
            # 
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
=======
            # Cache and return
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
            self._image_cache[path] = image
            return image
            
        except Exception as e:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            print(f"Error al cargar imagen {path}: {e}") # Print an error message if loading fails
            return None
        
    def play_sound(self, path):
        # Check cache
=======
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
            print(f"Error al cargar imagen {path}: {e}")
            return None
        
    def play_sound(self, path):
        """Carga un sonido, lo cachea y lo reproduce."""
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
            print(f"Error al cargar imagen {path}: {e}") # Print an error message if loading fails
            return None
        
    def play_sound(self, path):
        # Check cache
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
            print(f"Error al cargar imagen {path}: {e}") # Print an error message if loading fails
            return None
        
    def play_sound(self, path):
        # Check cache
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
            print(f"Error al cargar imagen {path}: {e}") # Print an error message if loading fails
            return None
        
    def play_sound(self, path):
        # Check cache
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        if path not in self._sound_cache:
            if not path or not os.path.exists(path):
                print(f"Error: No se encontró el sonido {path}")
                return
            try:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                # Charge from disk
=======
                # Carga del disco
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
                # Charge from disk
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
                # Carga del disco
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
                # Charge from disk
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
                # Carga del disco
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
                # Charge from disk
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
                self._sound_cache[path] = pygame.mixer.Sound(path)
            except Exception as e:
                print(f"Error al cargar sonido {path}: {e}")
                return
        
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # Play sound cached
        self._sound_cache[path].play()

    def add_item(self, item_id):
        # Add an item to the inventory
=======
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
        # Reproduce el sonido cacheado
        self._sound_cache[path].play()

    def add_item(self, item_id):
        """Añade un item al inventario global."""
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Play sound cached
        self._sound_cache[path].play()

    def add_item(self, item_id):
        # Add an item to the inventory
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Play sound cached
        self._sound_cache[path].play()

    def add_item(self, item_id):
        # Add an item to the inventory
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Play sound cached
        self._sound_cache[path].play()

    def add_item(self, item_id):
        # Add an item to the inventory
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        if item_id and item_id not in self.state["inventory"]:
            self.state["inventory"].append(item_id)
            print(f"[Engine] Item añadido: {item_id}")

    def set_var(self, var_name, value):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # Set a global state variable for example, "has_key" = True or "player_health" = 100
=======
        """Establece una variable de estado global."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Set a global state variable for example, "has_key" = True or "player_health" = 100
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
        """Establece una variable de estado global."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Set a global state variable for example, "has_key" = True or "player_health" = 100
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
        """Establece una variable de estado global."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Set a global state variable for example, "has_key" = True or "player_health" = 100
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        if var_name:
            self.state["game_vars"][var_name] = value
            print(f"[Engine] Variable: {var_name} = {value}")
    
    def get_var(self, var_name):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # Get a global state variable
        return self.state["game_vars"].get(var_name)
    
    def apply_effects(self, effects):
        # Apply a list of effects to the game state
=======
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
        """Consulta una variable de estado global."""
        return self.state["game_vars"].get(var_name)
    
    def apply_effects(self, effects):
        """Procesa una lista de efectos de datos (de ex_base.py)."""
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Get a global state variable
        return self.state["game_vars"].get(var_name)
    
    def apply_effects(self, effects):
        # Apply a list of effects to the game state
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Get a global state variable
        return self.state["game_vars"].get(var_name)
    
    def apply_effects(self, effects):
        # Apply a list of effects to the game state
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Get a global state variable
        return self.state["game_vars"].get(var_name)
    
    def apply_effects(self, effects):
        # Apply a list of effects to the game state
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                # The battle module to load is specified in the effect
                if e.get("battle_module"):
                    self.scene_manager.load_scene(e.get("battle_module"))
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
class Engine:
<<<<<<< HEAD
=======
class Engine:
>>>>>>> 9dd9a3f (Editing the main - engine - escene_maganer files and configuring them and eliminating extra files. I'm trying to do the first escene)
=======
class Engine:
>>>>>>> 9dd9a3f (Editing the main - engine - escene_maganer files and configuring them and eliminating extra files. I'm trying to do the first escene)
=======
class Engine:
>>>>>>> 9dd9a3f (Editing the main - engine - escene_maganer files and configuring them and eliminating extra files. I'm trying to do the first escene)
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} engine started.")


    def handle_event(self, event): # It means to handle events like keyboard input for the seleccion in the menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the event is to close the window
                running = False # It will stop the loop
            elif event.type == pygame.KEYDOWN:        # If a key is pressed
                if event.key == pygame.K_ESCAPE:      # If the key is Escape
                    pygame.quit() # It will close the window
                    sys.exit()  # And exit the program
                elif event.key == pygame.K_UP:          # If the key is the Up Arrow
                    print("Up") # It will print "Up"
                elif event.key == pygame.K_DOWN:        # If the key is the Up Arrow
                    print("Abajo") # It will print "Down"
                elif event.key == pygame.K_RETURN:    # If the key is Enter 
                    print("Enter") # It will print "Enter"
            
            self.Engine.handle_event(event)
    
    def update(self):
        self.all_sprites.update()

    def draw(self, screen):
        self.all_sprites.draw(screen)


    def stop(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        print(f"{self.name} engine stopped.")
>>>>>>> 9dd9a3f (Editing the main - engine - escene_maganer files and configuring them and eliminating extra files. I'm trying to do the first escene)
=======
    def __init__(self, name): # Constructor of the class
        self.name = Forsaken # Name of the engine
=======
    def __init__(self): # Constructor of the class
        self.name = None # Name of the engine
>>>>>>> b4d0ed7 (Run and debug)
        self.scene_manager = None # Scene manager of the engine
        self.screen = None # Screen of the engine
        self.clock = None # Clock of the engine
        self.quit_flag = False # Flag to indicate if the game should quit
>>>>>>> 32ed7b6 (Edition and comments of main.py)
=======
        self.state = {}
    
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
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

<<<<<<< HEAD
        self._font_cache[key] = f
        return f
    
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
        self._font_cache[key] = f # Cache the loaded font
        return f # Return the loaded font
    
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
=======
                # El motor es responsable de cargar escenas
=======
                # The battle module to load is specified in the effect
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
                if e.get("battle_module"):
                    self.scene_manager.load_scene(e.get("battle_module"))
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        print(f"{self.name} engine stopped.")
>>>>>>> 9dd9a3f (Editing the main - engine - escene_maganer files and configuring them and eliminating extra files. I'm trying to do the first escene)
=======
    def __init__(self, name): # Constructor of the class
        self.name = Forsaken # Name of the engine
=======
    def __init__(self): # Constructor of the class
        self.name = None # Name of the engine
>>>>>>> b4d0ed7 (Run and debug)
        self.scene_manager = None # Scene manager of the engine
        self.screen = None # Screen of the engine
        self.clock = None # Clock of the engine
        self.quit_flag = False # Flag to indicate if the game should quit
>>>>>>> 32ed7b6 (Edition and comments of main.py)
=======
        self.state = {}
    
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
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

<<<<<<< HEAD
        self._font_cache[key] = f
        return f
    
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
        self._font_cache[key] = f # Cache the loaded font
        return f # Return the loaded font
    
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
=======
                # El motor es responsable de cargar escenas
=======
                # The battle module to load is specified in the effect
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
                if e.get("battle_module"):
                    self.scene_manager.load_scene(e.get("battle_module"))
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        print(f"{self.name} engine stopped.")
>>>>>>> 9dd9a3f (Editing the main - engine - escene_maganer files and configuring them and eliminating extra files. I'm trying to do the first escene)
=======
    def __init__(self, name): # Constructor of the class
        self.name = Forsaken # Name of the engine
=======
    def __init__(self): # Constructor of the class
        self.name = None # Name of the engine
>>>>>>> b4d0ed7 (Run and debug)
        self.scene_manager = None # Scene manager of the engine
        self.screen = None # Screen of the engine
        self.clock = None # Clock of the engine
        self.quit_flag = False # Flag to indicate if the game should quit
>>>>>>> 32ed7b6 (Edition and comments of main.py)
=======
        self.state = {}
    
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
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

<<<<<<< HEAD
        self._font_cache[key] = f
        return f
    
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
        self._font_cache[key] = f # Cache the loaded font
        return f # Return the loaded font
    
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
=======
                # El motor es responsable de cargar escenas
=======
                # The battle module to load is specified in the effect
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
                if e.get("battle_module"):
                    self.scene_manager.load_scene(e.get("battle_module"))
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        print(f"{self.name} engine stopped.")
>>>>>>> 9dd9a3f (Editing the main - engine - escene_maganer files and configuring them and eliminating extra files. I'm trying to do the first escene)
=======
    def __init__(self, name): # Constructor of the class
        self.name = Forsaken # Name of the engine
=======
    def __init__(self): # Constructor of the class
        self.name = None # Name of the engine
>>>>>>> b4d0ed7 (Run and debug)
        self.scene_manager = None # Scene manager of the engine
        self.screen = None # Screen of the engine
        self.clock = None # Clock of the engine
        self.quit_flag = False # Flag to indicate if the game should quit
>>>>>>> 32ed7b6 (Edition and comments of main.py)
=======
        self.state = {}
    
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
=======
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

<<<<<<< HEAD
        self._font_cache[key] = f
        return f
    
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
        self._font_cache[key] = f # Cache the loaded font
        return f # Return the loaded font
    
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
