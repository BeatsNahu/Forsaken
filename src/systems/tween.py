import pygame

class Tween:
    def __init__(self, surface, start_pos, end_pos, duration_seconds, id=None, start_scale=1.0, end_scale=1.0, persist=False):
        self.id = id
        
        # --- NUEVO: Guardamos la imagen original ---
        # Esto es vital para evitar pérdida de calidad al re-escalar
        self.original_surface = surface 
        
        # La 'surface' actual será la que se re-escala cada frame
        self.surface = surface 
        
        # Posición (se refiere al CENTRO de la imagen)
        self.start_pos = pygame.Vector2(start_pos)
        self.end_pos = pygame.Vector2(end_pos)
        self.current_pos = pygame.Vector2(start_pos)
        
        # --- NUEVO: Propiedades de Escala ---
        self.start_scale = start_scale
        self.end_scale = end_scale
        self.current_scale = start_scale
        
        # Tiempo
        self.duration = max(0.01, duration_seconds)
        self.elapsed_time = 0.0
        self.is_finished = False

        # Persist
        self.persist = False
        
    def update(self, dt):
        """Actualiza la posición Y la escala."""
        if self.is_finished:
            return

        self.elapsed_time += dt
        progress = self.elapsed_time / self.duration
        
        if progress >= 1.0:
            progress = 1.0
            self.is_finished = True
            
        # 1. Interpolar Posición (Slide)
        self.current_pos = self.start_pos.lerp(self.end_pos, progress)
        
        # 2. Interpolar Escala (Zoom)
        # (Lerp manual para un solo número)
        self.current_scale = self.start_scale + (self.end_scale - self.start_scale) * progress
        
        # 3. Re-escalar la imagen original
        # Esto aplica el zoom
        new_width = int(self.original_surface.get_width() * self.current_scale)
        new_height = int(self.original_surface.get_height() * self.current_scale)
        
        # Evitar que la escala sea 0 (daría error)
        if new_width > 0 and new_height > 0:
            self.surface = pygame.transform.scale(self.original_surface, (new_width, new_height))

    def draw(self, surface_destino):
        """
        Dibuja la superficie escalada, centrada en su posición actual.
        """
        # Calcular la esquina superior izquierda (top-left) para que la
        # imagen quede centrada en self.current_pos
        draw_x = int(self.current_pos.x - self.surface.get_width() // 2)
        draw_y = int(self.current_pos.y - self.surface.get_height() // 2)
        
        surface_destino.blit(self.surface, (draw_x, draw_y))