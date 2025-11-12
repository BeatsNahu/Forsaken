import pygame
import config
from core.item_database import ITEM_DB  # Import the item DB

class InventoryMenu:
    def __init__(self, engine):
        self.engine = engine
        
        # --- 1. Load data ---
        # We use the list of item IDs directly from the engine state
        self.inventory_ids = self.engine.state.get("inventory", [])

        # --- 2. Navigation state ---
        self.selected_idx = 0     # For the main list
        self.details_visible = False  # For the details sub-UI
        self.detail_selection = 0   # 0 = "Usar", 1 = "Volver"
        self.detail_options = ["Usar", "Volver"]

        # --- 3. Load resources ---
        self.font = self.engine.load_font(config.FONT_PATH_DEFAULT, config.FONT_SIZE_REGULAR)
        self.font_title = self.engine.load_font(config.FONT_PATH_DEFAULT, config.FONT_SIZE_TITLE)
        self.font_desc = self.engine.load_font(config.FONT_PATH_DEFAULT, 22) # Slightly smaller

        self.sfx_swap = config.SFX_UI_SWAP
        self.sfx_confirm = config.SFX_UI_CONFIRM

        # UI images (you should create these)
        self.bg_panel = self.engine.load_image("assets/ui/inventory_bg.png")
        self.detail_panel = self.engine.load_image("assets/ui/item_details_bg.png")
        self.cursor = self.engine.load_image("assets/ui/inventory_cursor.png")

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        # --- State 1: Viewing item details ---
        if self.details_visible:
            if event.key == pygame.K_DOWN:
                self.detail_selection = (self.detail_selection + 1) % len(self.detail_options)
                self.engine.play_sound(self.sfx_swap, volume=0.5)
            elif event.key == pygame.K_UP:
                self.detail_selection = (self.detail_selection - 1) % len(self.detail_options)
                self.engine.play_sound(self.sfx_swap, volume=0.5)
            elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
                # Exit details view
                self.details_visible = False
                self.engine.play_sound(self.sfx_swap, volume=0.5)
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                selected_option = self.detail_options[self.detail_selection]
                
                if selected_option == "Usar":
                    self._use_item()
                elif selected_option == "Volver":
                    self.details_visible = False
                    self.engine.play_sound(self.sfx_swap, volume=0.5)
            
        # --- State 2: Navigating the list ---
        else:
            if event.key == pygame.K_ESCAPE:
                self.engine.pop_overlay() # Close the inventory
            elif event.key == pygame.K_DOWN:
                self.selected_idx = (self.selected_idx + 1) % max(1, len(self.inventory_ids))
                self.engine.play_sound(self.sfx_swap, volume=0.5)
            elif event.key == pygame.K_UP:
                self.selected_idx = (self.selected_idx - 1) % max(1, len(self.inventory_ids))
                self.engine.play_sound(self.sfx_swap, volume=0.5)
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                if self.inventory_ids: # Only if there are items
                    self.details_visible = True
                    self.detail_selection = 0 # Reset to "Usar"
                    self.engine.play_sound(self.sfx_confirm, volume=0.5)

    def _use_item(self):
        # 1. Get the item to use
        if not self.inventory_ids:
            return
        item_id = self.inventory_ids[self.selected_idx]
        item_data = ITEM_DB.get(item_id)

        if not item_data:
            print(f"Error: Item {item_id} no encontrado en ITEM_DB")
            return

        # 2. Get its effects
        effects = item_data.get("on_use_effects")

        # 3. Check if it's usable
        if effects is None:
            # Cannot be used
            self.engine.play_sound("assets/audio/sfx/error.ogg") # NEEDS THIS AUDIO
            self.engine.show_notification("No se puede usar este objeto.")
            return

        # 4. Apply the effects
        print(f"Usando item: {item_id}, aplicando efectos: {effects}")
        self.engine.apply_effects(effects)
        
        # 5. Remove the item from the global inventory
        self.engine.state["inventory"].pop(self.selected_idx)

        # 6. Refresh this UI (or simply close it)
        # Reload the list of IDs
        self.inventory_ids = self.engine.state.get("inventory", [])
        
        # Return to the main list
        self.details_visible = False
        self.selected_idx = min(self.selected_idx, len(self.inventory_ids) - 1)
        if self.selected_idx < 0:
            self.selected_idx = 0

    def update(self, dt):
        pass

    def draw(self, surface):
        # 1. Draw the main background panel
        if self.bg_panel:
            bg_rect = self.bg_panel.get_rect(center=surface.get_rect().center)
            surface.blit(self.bg_panel, bg_rect)
        else:
            pygame.draw.rect(surface, (20, 20, 40), (200, 100, 600, 800)) # Fallback

        # 2. Draw the item list
        start_x = 250
        start_y = 150
        spacing = 60
        
        if not self.inventory_ids:
            text_surf = self.font.render("Inventario vacío", True, config.COLOR_WHITE)
            surface.blit(text_surf, (start_x, start_y))
        
        for i, item_id in enumerate(self.inventory_ids):
            item_data = ITEM_DB.get(item_id, {})
            
            color = config.COLOR_YELLOW if i == self.selected_idx else config.COLOR_WHITE
            text = item_data.get("name", f"¡Error: {item_id}!")
            
            text_surf = self.font.render(text, True, color)
            surface.blit(text_surf, (start_x, start_y + i * spacing))
            
            if i == self.selected_idx and self.cursor:
                cursor_pos = (start_x - 50, start_y + i * spacing)
                surface.blit(self.cursor, cursor_pos)
                
    # 3. Draw the details sub-UI (if active)
        if self.details_visible and self.inventory_ids:
            item_id = self.inventory_ids[self.selected_idx]
            item = ITEM_DB.get(item_id, {})
            
            if self.detail_panel:
                detail_rect = self.detail_panel.get_rect(center=(surface.get_rect().centerx + 300, surface.get_rect().centery))
                surface.blit(self.detail_panel, detail_rect)
            else:
                pygame.draw.rect(surface, (30, 30, 50), (900, 200, 600, 600))
            
            detail_x = 920
            detail_y = 220
            
            name_surf = self.font_title.render(item.get("name"), True, config.COLOR_YELLOW)
            surface.blit(name_surf, (detail_x, detail_y))
            
            img_surf = self.engine.load_image(item.get("image"))
            if img_surf:
                img_surf_scaled = pygame.transform.scale(img_surf, (128, 128))
                surface.blit(img_surf_scaled, (detail_x, detail_y + 80))
            
            desc_surf = self.font_desc.render(item.get("description"), True, config.COLOR_WHITE)
            surface.blit(desc_surf, (detail_x, detail_y + 240))

            menu_start_y = detail_y + 350
            menu_spacing = 50

            for i, option_text in enumerate(self.detail_options):
                color = config.COLOR_YELLOW if i == self.detail_selection else config.COLOR_WHITE
                text_surf = self.font.render(option_text, True, color)
                surface.blit(text_surf, (detail_x, menu_start_y + i * menu_spacing))