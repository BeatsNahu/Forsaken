import pygame
import config

class ItemRewardOverlay:
    """An overlay that appears, shows an item with a rotating light,
    and disappears after a timeout or when a key is pressed.
    """
    def __init__(self, engine, item_name, item_image_path):
        self.engine = engine
        self.item_name = item_name
        
        # --- Load Resources ---
        self.font_title = self.engine.load_font(config.FONT_PATH_DEFAULT, config.FONT_SIZE_TITLE)
        self.font_item = self.engine.load_font(config.FONT_PATH_DEFAULT, config.FONT_SIZE_HUD)
        
        # Cargar imágenes
        self.item_image = self.engine.load_image(item_image_path)
        self.light_image_orig = self.engine.load_image("assets/vfx/light_reward.png", )
        
        # Escalar imágenes para que se vean bien
        if self.item_image:
            # Scale the item (e.g. from small sprites to a larger display)
            self.item_image = pygame.transform.scale(self.item_image, (2048, 2048))
        if self.light_image_orig:
            # Background light should be larger
            self.light_image_orig = pygame.transform.scale(self.light_image_orig, (512, 512))
        
        # --- Animation and control logic ---
        self.angle = 0.0
        self.rotation_speed = 40.0 # Degrees per second
        self.timer = 3.0 # Total time on screen (seconds)
        
        # Background veil (same as pause menu)
        self.veil = pygame.Surface(self.engine.screen.get_size(), pygame.SRCALPHA)
        self.veil.fill((0, 0, 0, 180)) # Semi-transparent black

    def handle_event(self, event):
        # Close on any key press
        if event.type == pygame.KEYDOWN:
            self.engine.pop_overlay()

    def update(self, dt):
        # 1. Rotate the light
        self.angle = (self.angle + self.rotation_speed * dt) % 360

        # 2. Countdown to auto-close
        self.timer -= dt
        if self.timer <= 0:
            self.engine.pop_overlay() # Pop this overlay from the stack

    def draw(self, surface):
        # 1. Draw background veil
        surface.blit(self.veil, (0, 0))

        # Central positions
        center_x = self.engine.screen.get_width() // 2
        center_y = self.engine.screen.get_height() // 2

        # 2. Draw the background light (rotated)
        if self.light_image_orig:
            # Rotate the original image (avoids degradation)
            rotated_light = pygame.transform.rotate(self.light_image_orig, self.angle)
            # Get the new rect centered
            light_rect = rotated_light.get_rect(center=(center_x, center_y))
            # Draw the rotated light
            surface.blit(rotated_light, light_rect)

        # 3. Draw the item (on top of the light)
        if self.item_image:
            item_rect = self.item_image.get_rect(center=(center_x, center_y))
            surface.blit(self.item_image, item_rect)

        # 4. Draw the texts
        title_surf = self.font_title.render("¡Objeto Obtenido!", True, config.COLOR_WHITE)
        title_rect = title_surf.get_rect(center=(center_x, center_y - 300))
        surface.blit(title_surf, title_rect)

        item_surf = self.font_item.render(self.item_name, True, config.COLOR_YELLOW)
        item_rect = item_surf.get_rect(center=(center_x, center_y + 300))
        surface.blit(item_surf, item_rect)