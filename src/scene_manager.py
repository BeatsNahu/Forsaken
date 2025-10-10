import importlib

class SceneManager: # Create a Game class to manage scene state
    def __init__(self, engine, scene_classes): # Initialize the game with a scene manager
        self.engine = engine # Reference to the game engine
        self.scene_classes = scene_classes # Dictionary of scene classes
        self.current_scene = None # Current active scene

    def load_scene(self, scene_name):
        mod = importlib.import_module(scene_name) # Dynamically import the module
        importlib.reload(mod) # Reload the module to get the latest changes
        if hasattr(mod, "SCENE_CLASS"):
            cls = mod.SCENE_CLASS
            scene = cls(self.engine)
        elif hasattr(mod, "SCENE"):
            data = mod.SCENE
            scene = self.scene_class(self.engine, data)
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
    def draw(self, screen):
        if self.current_scene:
            self.current_scene.draw(screen)

        