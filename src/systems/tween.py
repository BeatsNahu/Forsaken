# tween.py
import pygame

class Tween:
    """Represent a combined POSITION (slide) and SCALE (zoom) animation."""
    def __init__(self, surface, start_pos, end_pos, duration_seconds, id=None, start_scale=1.0, end_scale=1.0):
        self.id = id
        # Keep the original surface to avoid quality loss when re-scaling
        self.original_surface = surface

        # The current surface is the one that gets scaled each frame
        self.surface = surface

        # Position (refers to the image CENTER)
        self.start_pos = pygame.Vector2(start_pos)
        self.end_pos = pygame.Vector2(end_pos)
        self.current_pos = pygame.Vector2(start_pos)

        # Scale properties
        self.start_scale = start_scale
        self.end_scale = end_scale
        self.current_scale = start_scale

        # Time
        self.duration = max(0.01, duration_seconds)
        self.elapsed_time = 0.0
        self.is_finished = False

        # Persistence flag
        self.persist = persist

    def update(self, dt):
        if self.is_finished:
            return

        self.elapsed_time += dt
        progress = self.elapsed_time / self.duration

        if progress >= 1.0:
            progress = 1.0
            self.is_finished = True

        # 1. Interpolate position (slide)
        self.current_pos = self.start_pos.lerp(self.end_pos, progress)

        # 2. Interpolate scale (zoom)
        # (manual lerp for a single scalar)
        self.current_scale = self.start_scale + (self.end_scale - self.start_scale) * progress

        # 3. Rescale the original image
        # This applies the zoom
        new_width = int(self.original_surface.get_width() * self.current_scale)
        new_height = int(self.original_surface.get_height() * self.current_scale)

        # Avoid zero scale (would raise an error)
        if new_width > 0 and new_height > 0:
            self.surface = pygame.transform.scale(self.original_surface, (new_width, new_height))

    def draw(self, target_surface):
        """Draw the scaled surface centered at its current position on the
        provided target surface.
        """
        # Compute the top-left corner so the image is centered at current_pos
        draw_x = int(self.current_pos.x - self.surface.get_width() // 2)
        draw_y = int(self.current_pos.y - self.surface.get_height() // 2)

        target_surface.blit(self.surface, (draw_x, draw_y))