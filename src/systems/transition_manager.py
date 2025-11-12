import pygame
import config
class TransitionManager:
    def __init__(self, engine):
        self.engine = engine
        self.screen = engine.screen
        
        # State: "idle", "fading_out", "fading_in"
        self.state = "idle"
        self.alpha = 0  # Level of oscurity (255 = Totally dark) 
        self.speed = config.TRANSITION_SPEED # Velocity the fade 
        
        self.target_scene = None # The scene to load after fade out
        
        # Create a surface for the veil which has the screen size
        # SRCAHPLA allows do transparency
        self.veil = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.veil.fill((0, 0, 0, 0)) # Refill with transparent black

    def start_transition(self, target_scene_name: str):
        # Ready to start a transition if we are idle
        if self.state == "idle":
            self.target_scene = target_scene_name
            self.state = "fading_out"
            print(f"[Transition] Empezando fundido a negro hacia: {self.target_scene}")

    def update(self, dt: float):
        # Update 
        if self.state == "fading_out":
            self.alpha += self.speed * dt
            if self.alpha >= 255:
                self.alpha = 255
                # When
                self.engine.scene_manager.perform_scene_load(self.target_scene)
                # Start 
                self.state = "fading_in"
        
        elif self.state == "fading_in":
            self.alpha -= self.speed * dt
            if self.alpha <= 0:
                self.alpha = 0
                self.state = "idle"
                self.target_scene = None

    def draw(self, surface):
        # If 
        if self.state != "idle":
            # Refill 
            self.veil.fill((0, 0, 0, self.alpha))
            surface.blit(self.veil, (0, 0))

    def is_transitioning(self) -> bool:
        # Used f
        return self.state != "idle"