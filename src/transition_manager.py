# transition_manager.py
import pygame

class TransitionManager:
    def __init__(self, engine):
        self.engine = engine
        self.screen = engine.screen
        
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
        if self.state == "idle":
            self.target_scene = target_scene_name
            self.state = "fading_out"
            print(f"[Transition] Empezando fundido a negro hacia: {self.target_scene}")

    def update(self, dt: float):
        """Actualiza el estado del fundido (alpha)."""
        if self.state == "fading_out":
            self.alpha += self.speed * dt
            if self.alpha >= 255:
                self.alpha = 255
                # --- ¡PUNTO CLAVE! ---
                # Hemos llegado a negro. Ahora cargamos la nueva escena.
                self.engine.scene_manager.perform_scene_load(self.target_scene)
                # Y empezamos el fundido de entrada
                self.state = "fading_in"
        
        elif self.state == "fading_in":
            self.alpha -= self.speed * dt
            if self.alpha <= 0:
                self.alpha = 0
                self.state = "idle" # Terminamos la transición
                self.target_scene = None

    def draw(self, surface):
        """Dibuja el velo negro si no estamos inactivos."""
        if self.state != "idle":
            # Rellenamos el velo con el nivel de oscuridad (alpha) actual
            self.veil.fill((0, 0, 0, self.alpha))
            surface.blit(self.veil, (0, 0))

    def is_transitioning(self) -> bool:
        """Helper para saber si estamos en medio de un fundido."""
        return self.state != "idle"