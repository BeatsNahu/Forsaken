import pygame
<<<<<<< HEAD
from ui import DialogueBox, ChapterTitle
=======
import os

>>>>>>> d07fceb (Create def draw in the scene file to load data driven)

class Scene:
    def __init__(self, engine, data=None):
        # Store references and initialize runtime state
        self.engine = engine
        self.data = data or {}
        self.id = self.data.get("id", "unnamed")

<<<<<<< HEAD
        # Scene content
        self.background = self.data.get("background")
        self.lines = self.data.get("lines", [])
        self.choices = self.data.get("choices") or self.data.get("choises") or []

        # Runtime indexes and cached surfaces
        self._line_index = 0
        self._choice_index = 0
        self._bg_surf = None

        # Runtime UI components 
        self.ui = DialogueBox(self.engine) #

        # Chapter title component (if any)
        self.chapter_title = None
        if self.data.get("title"):
            self.chapter_title = ChapterTitle(self.engine, self.data.get("title"))

    def enter(self):
        # Load background image
        self._bg_surf = None
=======
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
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
        if self.background:
            path = self._normalize_path(self.background)
            try:
<<<<<<< HEAD
                surf = self.engine.load_image(self.background)
                if surf:
                    self._bg_surf = pygame.transform.scale(surf, self.engine.screen.get_size())
            except Exception as e:
                print(f"Error al cargar fondo {self.background}: {e}")
                self._bg_surf = None
        
        # Logic to play music and sound effects upon entering the scene
        # 1. Play continuous music
        music_path = self.data.get("music")
        if music_path:
            self.engine.play_music(music_path, loop=-1) # -1 = loop forever
        
        # 2. Play sound effect once
        sfx_path = self.data.get("sfx_on_enter")
        if sfx_path:
            self.engine.play_sound(sfx_path)

    def exit(self): 
        return # Placeholder for cleanup when a scene is replaced

    def handle_event(self, event):
        # If there is a chapter title being shown, block input until it finishes
        if self.chapter_title and not self.chapter_title.is_finished():
             return 

        # Handle keydown events for dialogue progression and choices
=======
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

    def exit(self):
        # Placeholder for cleanup when a scene is replaced
        return

    def handle_event(self, event):
        # Handle key events: advance text or navigate/select choices.
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
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
<<<<<<< HEAD
<<<<<<< HEAD
        
        if event.key == pygame.K_ESCAPE:
            setattr(self.engine, "quit_flag", True)

    def _advance(self):
        # Advance to the next line or show choices
        if self._line_index < len(self.lines):
            self._line_index += 1

            # Play SFX if the new line has one
            if self._line_index < len(self.lines):
                new_line = self.lines[self._line_index]
                if isinstance(new_line, dict):
                    sfx = new_line.get("sfx")
                    if sfx:
                        self.engine.play_sound(sfx)
                return

            # If we reached the end of lines, check for choices
            if self.choices:
                self._choice_index = 0 
                return
        
        # No more lines and no choices, go to next scene if specified
        if "next" in self.data:
            self.engine.apply_effects(self.data.get("effects", []))
            self.engine.scene_manager.load_scene(self.data["next"])

    def _choose(self, idx):
        if idx < 0 or idx >= len(self.choices):
            return
        
        choice = self.choices[idx]

        # Play choice SFX (if any)
        sfx = choice.get("sfx")
        if sfx:
            self.engine.play_sound(sfx)

        # Apply choice effects
        self.engine.apply_effects(choice.get("effects", [])) 
        
        # Load target scene
=======
=======
        if event.key == pygame.K_ESCAPE:
            setattr(self.engine, "quit_flag", True)
>>>>>>> b3233ed (feat: add escape key functionality to quit the game and delete images)

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
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
        target = choice.get("target") or choice.get("next") or choice.get("scene")
        if target:
            self.engine.scene_manager.load_scene(target)

<<<<<<< HEAD
    def update(self, dt):
        # Update chapter title (if any)
        if self.chapter_title:
            self.chapter_title.update(dt)

    def draw(self, surface):
        # 1. Draw background 
=======
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
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
        if self._bg_surf:
            surface.blit(self._bg_surf, (0, 0)) # Draw background image
        else:
            surface.fill((0, 0, 0))
<<<<<<< HEAD
        
        # HERE I WILL CREATE ANIMATION_MANAGER TO HANDLE ANIMATED BACKGROUNDS LATER

        # 2. Draw dialogue box or choices
        if self._is_showing_choices():
            self.ui.draw(surface, text=None, choices=self.choices, choice_idx=self._choice_index)
        
        elif self.lines:
            ln = self.lines[self._line_index]
            text = ln.get("text", "") if isinstance(ln, dict) else str(ln)
            speaker = ln.get("speaker") if isinstance(ln, dict) else None
            
            self.ui.draw(surface, text=text, speaker=speaker)

        # 3. Draw chapter title (if any)
        if self.chapter_title:
            self.chapter_title.draw(surface)
   
    def _is_showing_choices(self):
        # Returns True if we are at the end of lines and have choices to show
        return self._line_index == len(self.lines) and bool(self.choices)
=======

        title = self.data.get("title")
        # Title: centered at the top of the screen
        if title and self.title_font:
            surf = self.title_font.render(title, True, (255, 255, 255))
            surface.blit(surf, ((surface.get_width() - surf.get_width()) // 2, 20))

        # Current dialog/text: centered near the bottom of the screen
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
                surface.blit(txt_surf, (80, surface.get_height() - 150))

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
        return self._line_index >= max(0, len(self.lines) - 1) and bool(self.choices) # The utility function checks if the scene is currently displaying choices to the player

    def _normalize_path(self, p):
        # If path exists return it; otherwise try dotted->filesystem conversion
<<<<<<< HEAD
        if os.path.exists(p):
            return p
        parts = p.split('.')
        if len(parts) >= 3:
            newp = os.path.join(*parts[:-1]) + '.' + parts[-1]
            if os.path.exists(newp):
                return newp
        return p
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
        if os.path.exists(p): # If the path exists,
            return p # return it as is
        parts = p.split('.') # Split the path by dots
        if len(parts) >= 3: # If there are at least 3 parts,
            newp = os.path.join(*parts[:-1]) + '.' + parts[-1] # Join all parts except the last one with os separators and add the last part with a dot
            if os.path.exists(newp): # If the new path exists,
                return newp # return the new path
        return p # Return the original path if no valid path is found
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
