import importlib

class SceneManager: # Create a Game class to manage scene state
    def __init__(self, engine, scene_classes): # Initialize the game with a scene manager
        self.engine = engine # Reference to the game engine
        self.scene_classes = scene_classes # Dictionary of scene classes
        self.current_scene = None # Current active scene

    def load_scene(self, scene_name):
        mod = importlib.import_module(scene_name) # Dynamically import the module
        importlib.reload(mod) # Reload the module to get the latest changes
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
            if cls:
                scene = cls(self.engine, data)
            else:
                scene = BaseScene(self.engine, data)
        elif hasattr(mod, "create") and callable(mod.create):
            scene = mod.create(self.engine)   
        else:
            raise RuntimeError("Módulo de escena inválido: " + scene_name)

        if self.current_scene and hasattr(self.current_scene, "exit"):
            self.current_scene.exit()
        self.current_scene = scene
        self.engine.state["current_scene"] = getattr(scene, "id", None)
        scene.enter()
        return scene

    def handle_event(self, event): # Handle events and delegate to the current scene
        if self.current_scene: # If there is a current scene
            self.current_scene.handle_event(event) # Delegate event handling to the current scene
    
    def update(self, dt): # Update the current scene with delta time, so the FPS will be the same on every computer
        if self.current_scene:
            self.current_scene.update(dt)

    def draw(self, screen): # Draw the current scene
        if self.current_scene:
            self.current_scene.draw(screen)

        