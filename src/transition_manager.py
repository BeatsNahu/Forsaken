<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
# transition_manager.py
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
# transition_manager.py
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
# transition_manager.py
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
import pygame

class TransitionManager:
    def __init__(self, engine):
        self.engine = engine
        self.screen = engine.screen
        
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # State: "idle", "fading_out", "fading_in"
        self.state = "idle"
        self.alpha = 0  # Level of oscurity (255 = Totally dark) 
        self.speed = 500 # Velocity the fade 
        
        self.target_scene = None # The scene to load after fade out
        
        # Create a surface for the veil which has the screen size
        # SRCAHPLA allows do transparency
        self.veil = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.veil.fill((0, 0, 0, 0)) # Refill with transparent black

    def start_transition(self, target_scene_name: str):
        # Ready to start a transition if we are idle
=======
        # Estado: "idle", "fading_out" (volviéndose negro), "fading_in" (aclarando)
=======
        # State: "idle", "fading_out", "fading_in"
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        self.state = "idle"
        self.alpha = 0  # Level of oscurity (255 = Totally dark) 
        self.speed = 500 # Velocity the fade 
        
        self.target_scene = None # The scene to load after fade out
        
        # Create a surface for the veil which has the screen size
        # SRCAHPLA allows do transparency
        self.veil = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.veil.fill((0, 0, 0, 0)) # Refill with transparent black

    def start_transition(self, target_scene_name: str):
<<<<<<< HEAD
        """Inicia el proceso de fundido para cargar una nueva escena."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Ready to start a transition if we are idle
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
        # Estado: "idle", "fading_out" (volviéndose negro), "fading_in" (aclarando)
=======
        # State: "idle", "fading_out", "fading_in"
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        self.state = "idle"
        self.alpha = 0  # Level of oscurity (255 = Totally dark) 
        self.speed = 500 # Velocity the fade 
        
        self.target_scene = None # The scene to load after fade out
        
        # Create a surface for the veil which has the screen size
        # SRCAHPLA allows do transparency
        self.veil = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.veil.fill((0, 0, 0, 0)) # Refill with transparent black

    def start_transition(self, target_scene_name: str):
<<<<<<< HEAD
        """Inicia el proceso de fundido para cargar una nueva escena."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Ready to start a transition if we are idle
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
        # Estado: "idle", "fading_out" (volviéndose negro), "fading_in" (aclarando)
=======
        # State: "idle", "fading_out", "fading_in"
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        self.state = "idle"
        self.alpha = 0  # Level of oscurity (255 = Totally dark) 
        self.speed = 500 # Velocity the fade 
        
        self.target_scene = None # The scene to load after fade out
        
        # Create a surface for the veil which has the screen size
        # SRCAHPLA allows do transparency
        self.veil = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.veil.fill((0, 0, 0, 0)) # Refill with transparent black

    def start_transition(self, target_scene_name: str):
<<<<<<< HEAD
        """Inicia el proceso de fundido para cargar una nueva escena."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Ready to start a transition if we are idle
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        if self.state == "idle":
            self.target_scene = target_scene_name
            self.state = "fading_out"
            print(f"[Transition] Empezando fundido a negro hacia: {self.target_scene}")

    def update(self, dt: float):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # Update 
=======
        """Actualiza el estado del fundido (alpha)."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Update 
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
        """Actualiza el estado del fundido (alpha)."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Update 
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
        """Actualiza el estado del fundido (alpha)."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Update 
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        if self.state == "fading_out":
            self.alpha += self.speed * dt
            if self.alpha >= 255:
                self.alpha = 255
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                # When
                self.engine.scene_manager.perform_scene_load(self.target_scene)
                # Start 
=======
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
                # --- ¡PUNTO CLAVE! ---
                # Hemos llegado a negro. Ahora cargamos la nueva escena.
                self.engine.scene_manager.perform_scene_load(self.target_scene)
                # Y empezamos el fundido de entrada
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
                # When
                self.engine.scene_manager.perform_scene_load(self.target_scene)
                # Start 
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
                # When
                self.engine.scene_manager.perform_scene_load(self.target_scene)
                # Start 
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
                # When
                self.engine.scene_manager.perform_scene_load(self.target_scene)
                # Start 
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
                self.state = "fading_in"
        
        elif self.state == "fading_in":
            self.alpha -= self.speed * dt
            if self.alpha <= 0:
                self.alpha = 0
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                self.state = "idle"
                self.target_scene = None

    def draw(self, surface):
        # If 
        if self.state != "idle":
            # Refill 
=======
                self.state = "idle" # Terminamos la transición
=======
                self.state = "idle"
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
                self.target_scene = None

    def draw(self, surface):
        # If 
        if self.state != "idle":
<<<<<<< HEAD
            # Rellenamos el velo con el nivel de oscuridad (alpha) actual
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
            # Refill 
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
                self.state = "idle" # Terminamos la transición
=======
                self.state = "idle"
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
                self.target_scene = None

    def draw(self, surface):
        # If 
        if self.state != "idle":
<<<<<<< HEAD
            # Rellenamos el velo con el nivel de oscuridad (alpha) actual
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
            # Refill 
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
                self.state = "idle" # Terminamos la transición
=======
                self.state = "idle"
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
                self.target_scene = None

    def draw(self, surface):
        # If 
        if self.state != "idle":
<<<<<<< HEAD
            # Rellenamos el velo con el nivel de oscuridad (alpha) actual
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
            # Refill 
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
            self.veil.fill((0, 0, 0, self.alpha))
            surface.blit(self.veil, (0, 0))

    def is_transitioning(self) -> bool:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        # Used f
=======
        """Helper para saber si estamos en medio de un fundido."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Used f
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
        """Helper para saber si estamos en medio de un fundido."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Used f
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
=======
        """Helper para saber si estamos en medio de un fundido."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        # Used f
>>>>>>> 66d7783 (refactor: clean up comments and improve event handling in BattleManager and SceneManager.)
        return self.state != "idle"