import pygame


class Tween:
    def __init__(self, surface, start_pos, end_pos, duration_seconds, id=None, start_scale=1.0, end_scale=1.0, persist=False):
        self.id = id

        # --- NEW: Keep the original image ---
        # This is vital to avoid quality loss when re-scaling
        self.original_surface = surface

        # The current surface is the one that gets re-scaled each frame
        self.surface = surface

        # Position (refers to the CENTER of the image)
        self.start_pos = pygame.Vector2(start_pos)
        self.end_pos = pygame.Vector2(end_pos)
        self.current_pos = pygame.Vector2(start_pos)

        # --- NEW: Scale properties ---
        self.start_scale = start_scale
        self.end_scale = end_scale
        self.current_scale = start_scale

        # Time
        self.duration = max(0.01, duration_seconds)
        self.elapsed_time = 0.0
        self.is_finished = False

        # Persist
        self.persist = persist

    def update(self, dt):
        """Update position AND scale."""
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

        # 3. Re-scale the original image
        # This applies the zoom
        new_width = int(self.original_surface.get_width() * self.current_scale)
        new_height = int(self.original_surface.get_height() * self.current_scale)

        # Avoid zero scale (would raise an error)
        if new_width > 0 and new_height > 0:
            self.surface = pygame.transform.scale(self.original_surface, (new_width, new_height))

    def draw(self, surface_destino):
        # Compute the top-left corner so the image is centered at self.current_pos
        draw_x = int(self.current_pos.x - self.surface.get_width() // 2)
        draw_y = int(self.current_pos.y - self.surface.get_height() // 2)

        surface_destino.blit(self.surface, (draw_x, draw_y))