import pygame
import os


class Scene:
    def __init__(self, engine, data=None):
        # Store references and initialize runtime state
        self.engine = engine
        self.data = data or {}
        self.id = self.data.get("id", "unnamed")

        # scene content
        self.background = self.data.get("background")
        self.lines = self.data.get("lines", [])
        # accept both 'choices' and misspelled 'choises'
        self.choices = self.data.get("choices") or self.data.get("choises") or []

        # runtime indexes and cached surfaces
        self._line_index = 0
        self._choice_index = 0
        self._bg_surf = None
        self.font = None
        self.title_font = None

    def enter(self):
        # Load background image (if provided) and initialize fonts. Non-fatal on error.
        if self.background:
            path = self._normalize_path(self.background)
            try:
                surf = pygame.image.load(path)
                self._bg_surf = pygame.transform.scale(surf, self.engine.screen.get_size())
            except Exception:
                self._bg_surf = None

        # Prefer the bundled 'press-start.k.ttf' if available, otherwise fall back
        # to the default pygame font. Use different sizes for body and title.
        font_path = os.path.join("assets", "fonts", "press-start.k.ttf")
        try:
            if os.path.exists(font_path):
                self.font = pygame.font.Font(font_path, 20)
                self.title_font = pygame.font.Font(font_path, 40)
            else:
                # fallback to default font
                self.font = pygame.font.Font(None, 28)
                self.title_font = pygame.font.Font(None, 48)
        except Exception:
            self.font = None
            self.title_font = None

        # optional music control via engine
        music = self.data.get("music")
        if music and hasattr(self.engine, "play_music"):
            try:
                self.engine.play_music(music)
            except Exception:
                pass

    def exit(self):
        # Placeholder for cleanup when a scene is replaced
        return

    def handle_event(self, event):
        # Handle key events: advance text or navigate/select choices.
        if event.type != pygame.KEYDOWN:
            return

        if self._is_showing_choices():
            if event.key == pygame.K_DOWN:
                self._choice_index = (self._choice_index + 1) % max(1, len(self.choices))
            elif event.key == pygame.K_UP:
                self._choice_index = (self._choice_index - 1) % max(1, len(self.choices))
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self._choose(self._choice_index)
        else:
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self._advance()

    def _advance(self):
        # Move to the next line, reveal choices, or follow the 'next' key.
        if self._line_index < len(self.lines) - 1:
            self._line_index += 1
            return

        if self.choices:
            self._choice_index = 0
            return

        if "next" in self.data:
            self.apply_effects(self.data.get("effects", []))
            self.engine.scene_manager.load_scene(self.data["next"])

    def _choose(self, idx):
        # Execute effects for the chosen option and navigate if a target exists.
        if idx < 0 or idx >= len(self.choices):
            return
        choice = self.choices[idx]
        self.apply_effects(choice.get("effects", []))
        target = choice.get("target") or choice.get("next") or choice.get("scene")
        if target:
            self.engine.scene_manager.load_scene(target)

    def apply_effects(self, effects):
        # Apply simple, engine-specific effects described as dicts.
        for e in effects:
            if not isinstance(e, dict):
                continue
            t = e.get("type")
            if t == "give_item" and hasattr(self.engine, "add_item"):
                self.engine.add_item(e.get("item"))
            elif t == "set_var" and hasattr(self.engine, "set_var"):
                self.engine.set_var(e.get("name"), e.get("value"))
            elif t == "start_battle":
                if e.get("battle_module"):
                    self.engine.scene_manager.load_scene(e.get("battle_module"))

    def update(self, dt):
        # Per-frame updates (no-op by default).
        return

    def draw(self, surface):
        # Draw background, title, current dialog line, and choices.
        if self._bg_surf:
            surface.blit(self._bg_surf, (0, 0))
        else:
            surface.fill((0, 0, 0))

        title = self.data.get("title")
        if title and self.title_font:
            surf = self.title_font.render(title, True, (255, 255, 255))
            surface.blit(surf, (50, 30))

        if self.lines:
            ln = self.lines[self._line_index]
            if isinstance(ln, dict):
                text = ln.get("text", "")
                speaker = ln.get("speaker")
                display = f"{speaker}: {text}" if speaker else text
            else:
                display = str(ln)
            if self.font:
                txt_surf = self.font.render(display, True, (255, 255, 255))
                surface.blit(txt_surf, (60, 200))

        if self._line_index >= max(0, len(self.lines) - 1) and self.choices:
            base_y = 300
            for i, c in enumerate(self.choices):
                text = c.get("text") or str(c)
                color = (255, 255, 0) if i == self._choice_index else (255, 255, 255)
                if self.font:
                    txt = self.font.render(text, True, color)
                    surface.blit(txt, (80, base_y + i * 40))

    def _is_showing_choices(self):
        # True when at last line and choices exist
        return self._line_index >= max(0, len(self.lines) - 1) and bool(self.choices)

    def _normalize_path(self, p):
        # If path exists return it; otherwise try dotted->filesystem conversion
        if os.path.exists(p):
            return p
        parts = p.split('.')
        if len(parts) >= 3:
            newp = os.path.join(*parts[:-1]) + '.' + parts[-1]
            if os.path.exists(newp):
                return newp
        return p
