import importlib
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
import pygame
from scene import Scene as BaseScene
class SceneManager: # Create a Game class to manage scene state
    def __init__(self, engine, scene_classes): # Initialize the game with a scene manager
=======

class SceneManager: # Create a Game class to manage scene state
    def __init__(self): # Initialize the game with a scene manager
>>>>>>> 32ed7b6 (Edition and comments of main.py)
        self.engine = engine # Reference to the game engine
        self.scene_classes = scene_classes # Dictionary of scene classes
        self.current_scene = None # Current active scene

    def load_scene(self, scene_name):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # Using the transition manager to load the scene with a fade effect
        if not self.engine.transition_manager.is_transitioning(): # Only load scene if not already transitioning
            self.engine.transition_manager.start_transition(scene_name) # Start the transition to the new scene
=======
        """
        Método PÚBLICO para solicitar un cambio de escena.
        Inicia el fundido a negro (fade-out).
        """
        # No cargamos la escena AHORA.
        # Se lo pedimos al gestor de transiciones.
        if not self.engine.transition_manager.is_transitioning():
            self.engine.transition_manager.start_transition(scene_name)
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Using the transition manager to load the scene with a fade effect
        if not self.engine.transition_manager.is_transitioning(): # Only load scene if not already transitioning
            self.engine.transition_manager.start_transition(scene_name) # Start the transition to the new scene
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        else:
            print(f"Advertencia: Se intentó cargar {scene_name} durante una transición.")

    def perform_scene_load(self, scene_name):
        mod = importlib.import_module(scene_name) # Dynamically import the module
        importlib.reload(mod) # Reload the module to get the latest changes
        
        scene = None 

        if hasattr(mod, "SCENE_CLASS"): # If the module has a SCENE_CLASS attribute, use it to create the scene
            cls = mod.SCENE_CLASS # Get the scene class
            scene = cls(self.engine) # Create an instance of the scene class
        elif hasattr(mod, "SCENE"): # If the module has a SCENE attribute, use it to create the scene
            data = mod.SCENE # Get the scene data
            # scene_classes may be a class or a mapping; try to instantiate with provided scene_classes
            if isinstance(self.scene_classes, dict):
                # try to resolve class name from data, or take any class in the mapping as fallback
                cls = self.scene_classes.get(data.get("class")) or next(iter(self.scene_classes.values()), None)
            else:
                cls = self.scene_classes
            # Fallback to the base Scene class from scene module
            from scene import Scene as BaseScene
            if cls: # If a scene class is found, create an instance of it
                scene = cls(self.engine, data) # Create an instance of the scene class
            else:
                scene = BaseScene(self.engine, data) # Create an instance of the base Scene class
        elif hasattr(mod, "create") and callable(mod.create): # If the module has a create function, use it to create the scene
            scene = mod.create(self.engine) # Call the create function to get the scene instance
<<<<<<< HEAD
        else:
            raise RuntimeError("Módulo de escena inválido: " + scene_name) # Raise an error if the module is invalid

        if self.current_scene and hasattr(self.current_scene, "exit"):
            self.current_scene.exit()
        self.current_scene = scene
        self.engine.state["current_scene"] = getattr(scene, "id", None)
        scene.enter()
        return scene

    def handle_event(self, event): # Handle events and delegate to the current scene
        # If we are in transition, ignore all events except quitting
        if self.engine.transition_manager.is_transitioning():
            # only handle quit events
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                setattr(self.engine, "quit_flag", True)
            return

        # If not in transition, pass events to the current scene
        if self.current_scene:
            self.current_scene.handle_event(event)
        
    def update(self, dt): # Update the current scene with delta time, so the FPS will be the same on every computer
        # Update the transition manager first
        self.engine.transition_manager.update(dt)

        # Only update the current scene if not in transition
        if self.current_scene and not self.engine.transition_manager.is_transitioning():
            self.current_scene.update(dt)

    def draw(self, screen): # Draw the current scene
        # Draw the current scene all the time
        if self.current_scene:
            self.current_scene.draw(screen)
            
        # Draw/Show the transition effect on top of the current scene
        self.engine.transition_manager.draw(screen)
=======
        mod = importlib.import_module(module.path) # Dynamically import the module
        importlib.reload(mod) # Reload the module to get the latest changes
        if hasattr(mod, "SCENE_CLASS"):
            cls = mod.SCENE_CLASS
            scene = cls(self.engine)
        elif hasattr(mod, "SCENE"):
            data = mod.SCENE
            scene = self.scene_class(self.engine, data)
        elif hasattr(mod, "create") and callable(mod.create):
            scene = mod.create(self.engine)   
=======
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
        else:
            raise RuntimeError("Módulo de escena inválido: " + scene_name) # Raise an error if the module is invalid

        if self.current_scene and hasattr(self.current_scene, "exit"):
            self.current_scene.exit()
        self.current_scene = scene
        self.engine.state["current_scene"] = getattr(scene, "id", None)
        scene.enter()
        return scene

    def handle_event(self, event): # Handle events and delegate to the current scene
        # If we are in transition, ignore all events except quitting
        if self.engine.transition_manager.is_transitioning():
            # only handle quit events
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                setattr(self.engine, "quit_flag", True)
            return

        # If not in transition, pass events to the current scene
        if self.current_scene:
            self.current_scene.handle_event(event)
        
    def update(self, dt): # Update the current scene with delta time, so the FPS will be the same on every computer
        # Update the transition manager first
        self.engine.transition_manager.update(dt)

        # Only update the current scene if not in transition
        if self.current_scene and not self.engine.transition_manager.is_transitioning():
            self.current_scene.update(dt)

    def draw(self, screen): # Draw the current scene
        # Draw the current scene all the time
        if self.current_scene:
            self.current_scene.draw(screen)
<<<<<<< HEAD
>>>>>>> 32ed7b6 (Edition and comments of main.py)
=======
            
        # Draw/Show the transition effect on top of the current scene
        self.engine.transition_manager.draw(screen)
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)

        