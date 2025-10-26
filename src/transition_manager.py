<<<<<<< HEAD
=======
# transition_manager.py
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
import pygame

class TransitionManager:
    def __init__(self, engine):
        self.engine = engine
        self.screen = engine.screen
        
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
        self.state = "idle"
        self.alpha = 0  # Nivel de oscuridad (0 = transparente, 255 = negro)
        self.speed = 500  # Velocidad del fundido (píxeles de alfa por segundo)
        
        self.target_scene = None # La escena a la que queremos ir
        
        # Creamos una superficie (Surface) del tamaño de la pantalla
        # SRCAHPLA permite que la superficie maneje transparencia por píxel
        self.veil = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.veil.fill((0, 0, 0, 0)) # Rellenar con negro transparente

    def start_transition(self, target_scene_name: str):
        """Inicia el proceso de fundido para cargar una nueva escena."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
        if self.state == "idle":
            self.target_scene = target_scene_name
            self.state = "fading_out"
            print(f"[Transition] Empezando fundido a negro hacia: {self.target_scene}")

    def update(self, dt: float):
<<<<<<< HEAD
        # Update 
=======
        """Actualiza el estado del fundido (alpha)."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
        if self.state == "fading_out":
            self.alpha += self.speed * dt
            if self.alpha >= 255:
                self.alpha = 255
<<<<<<< HEAD
                # When
                self.engine.scene_manager.perform_scene_load(self.target_scene)
                # Start 
=======
                # --- ¡PUNTO CLAVE! ---
                # Hemos llegado a negro. Ahora cargamos la nueva escena.
                self.engine.scene_manager.perform_scene_load(self.target_scene)
                # Y empezamos el fundido de entrada
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
                self.state = "fading_in"
        
        elif self.state == "fading_in":
            self.alpha -= self.speed * dt
            if self.alpha <= 0:
                self.alpha = 0
<<<<<<< HEAD
                self.state = "idle"
                self.target_scene = None

    def draw(self, surface):
        # If 
        if self.state != "idle":
            # Refill 
=======
                self.state = "idle" # Terminamos la transición
                self.target_scene = None

    def draw(self, surface):
        """Dibuja el velo negro si no estamos inactivos."""
        if self.state != "idle":
            # Rellenamos el velo con el nivel de oscuridad (alpha) actual
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
            self.veil.fill((0, 0, 0, self.alpha))
            surface.blit(self.veil, (0, 0))

    def is_transitioning(self) -> bool:
<<<<<<< HEAD
        # Used f
=======
        """Helper para saber si estamos en medio de un fundido."""
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
        return self.state != "idle"