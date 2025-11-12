import pygame
import os
import config
from overlays.item_reward import ItemRewardOverlay
class Engine:
    def __init__(self): # Builder of the engine
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
        self.transition_manager = None
        self.animation_manager = None

        # Overlays
        self.overlay_stack = []

        # Simple resource caches
        self._font_cache = {}
        self._image_cache = {}
        self._sound_cache = {}

        self._current_music_path = None

        # Notification system
        self.notifications = []
        self.notifications_font = self.load_font(config.FONT_PATH_DEFAULT, config.FONT_SIZE_LOG) # Default font for notifications

    def play_music(self, path, loop=-1, volume=config.DEFAULT_MUSIC_VOLUME):
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
            
            # Cache and return
            self._image_cache[path] = image
            return image
            
        except Exception as e:
            print(f"Error al cargar imagen {path}: {e}") # Print an error message if loading fails
            return None

    def play_sound(self, path, volume=config.DEFAULT_SFX_VOLUME):
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
        
        # Logic to set volume before playing sound
        sound_obj = self._sound_cache[path]
        channel = sound_obj.play()
        if channel:
            channel.set_volume(volume)

    def add_item(self, item_id):
        # Add an item to the inventory
        if item_id and item_id not in self.state["inventory"]:
            self.state["inventory"].append(item_id)
            print(f"[Engine] Item añadido: {item_id}")

    def set_var(self, var_name, value):
        if not var_name or value is None:
            return

        # Si es un string que empieza con '+' o '-', lo interpretamos como incremento
        if isinstance(value, str) and value.startswith(("+", "-")):
            current = self.state["game_vars"].get(var_name, 0)
            try:
                self.state["game_vars"][var_name] = current + int(value)
            except ValueError:
                print(f"[Engine] Valor inválido para set_var: {value}")
        else:
            # Sobrescribe directamente
            self.state["game_vars"][var_name] = value
        print(f"[Engine] Variable: {var_name} = {self.state['game_vars'][var_name]}")

    
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
            
            elif t == "notify":
                text = e.get("text", "¡Algo ha cambiado!")
                duration = e.get("duration", 3.0)
                self.show_notification(text, duration)

            elif t == "show_item_overlay":
                item_name = e.get("item_name", "???")
                item_image = e.get("item_image")
                
                # Only show overlay if we have an image
                if item_image:
                    self.push_overlay(ItemRewardOverlay(self, item_name, item_image))
                else:
                    print(f"Error: show_item_overlay no tiene 'item_image'")

    def show_notification(self, text, duration=2.0):
        # Show a notification on the screen for a certain duration (in seconds)
        self.notifications.append({"text": text, "timer": duration})
    
    def _update_notifications(self, dt):
        # Update the notification timers and remove expired ones
        new_list = []
        for notif in self.notifications[:]:
            notif["timer"] -= dt
            if notif["timer"] > 0:
                new_list.append(notif)
        self.notifications = new_list

    def _draw_notifications(self, surface):
        # Draw notifications on the screen
        if not self.notifications:
            return
        
        notif = self.notifications[0]  # Show only the first notification for simplicity
        text_surf = self.notifications_font.render(notif["text"], True, config.COLOR_WHITE)  # White color

        # Position at top-left corner with some padding
        pos_x = (surface.get_width() - text_surf.get_width()) // 2
        surface.blit(text_surf, (pos_x, config.NOTIFICATION_PADDING_Y))

    # Overlays management
    def push_overlay(self, overlay):
        # Añade un overlay a la cima de la pila.
        print(f"[Engine] Pushing overlay: {overlay.__class__.__name__}")
        self.overlay_stack.append(overlay)

    def pop_overlay(self):
        # Elimina el overlay de la cima de la pila.
        if self.overlay_stack:
            overlay = self.overlay_stack.pop()
            print(f"[Engine] Popping overlay: {overlay.__class__.__name__}")
            return overlay
        return None

    def get_top_overlay(self):
        # Devuelve el overlay de la cima (el que está activo) sin quitarlo.
        if self.overlay_stack:
            return self.overlay_stack[-1]
        return None

    def update_overlays(self, dt):
        # Actualiza SÓLO el overlay que está en la cima.
        top_overlay = self.get_top_overlay()
        if top_overlay and hasattr(top_overlay, "update"):
            top_overlay.update(dt)

    def draw_overlays(self, surface):
        # Dibuja TODOS los overlays, de abajo hacia arriba.
        for overlay in self.overlay_stack:
            if hasattr(overlay, "draw"):
                overlay.draw(surface)