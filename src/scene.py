<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import pygame
<<<<<<< HEAD
<<<<<<< HEAD
from ui import DialogueBox, ChapterTitle
=======
import os
<<<<<<< HEAD

>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
from ui import DialogueBox, ChapterTitle #
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
from ui import DialogueBox, ChapterTitle
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)

class Scene:
    def __init__(self, engine, data=None):
        # Store references and initialize runtime state
        self.engine = engine
        self.data = data or {}
        self.id = self.data.get("id", "unnamed")

<<<<<<< HEAD
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
=======
        # Scene content
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
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
<<<<<<< HEAD
<<<<<<< HEAD
        # Load background image (if provided) and initialize fonts. Non-fatal on error.
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
        if self.background:
            path = self._normalize_path(self.background)
<<<<<<< HEAD
            try:
<<<<<<< HEAD
=======
        # --- ARREGLADO ---
        # Código de fondo limpiado. Eliminado el error de 'path'.
        self._bg_surf = None # Empezar como None
=======
        # Load background image
        self._bg_surf = None
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
        if self.background:
            try:
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
                surf = self.engine.load_image(self.background)
                if surf:
                    self._bg_surf = pygame.transform.scale(surf, self.engine.screen.get_size())
            except Exception as e:
                print(f"Error al cargar fondo {self.background}: {e}")
                self._bg_surf = None
        
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
        # Logic to play music and sound effects upon entering the scene
        # 1. Play continuous music
        music_path = self.data.get("music")
        if music_path:
            self.engine.play_music(music_path, loop=-1) # -1 = loop forever
        
        # 2. Play sound effect once
        sfx_path = self.data.get("sfx_on_enter")
        if sfx_path:
            self.engine.play_sound(sfx_path)
<<<<<<< HEAD

    def exit(self): 
        return # Placeholder for cleanup when a scene is replaced

    def handle_event(self, event):
        # If there is a chapter title being shown, block input until it finishes
        if self.chapter_title and not self.chapter_title.is_finished():
             return 

        # Handle keydown events for dialogue progression and choices
=======
                surf = pygame.image.load(path)
=======
        try:
        # ANTES: surf = pygame.image.load(path)
            surf = self.engine.load_image(path) # <--- MODIFICADO
            if surf:
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
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
=======
        # ¡YA NO SE CARGAN FUENTES AQUÍ! La UI lo hace.
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)

    def exit(self): 
        return # Placeholder for cleanup when a scene is replaced

    def handle_event(self, event):
<<<<<<< HEAD
<<<<<<< HEAD
        # Handle key events: advance text or navigate/select choices.
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
        # Si el título se está mostrando, bloquear input
        if self.chapter_title and not self.chapter_title.is_finished(): #
             return 

>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
        # If there is a chapter title being shown, block input until it finishes
        if self.chapter_title and not self.chapter_title.is_finished():
             return 

        # Handle keydown events for dialogue progression and choices
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
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
<<<<<<< HEAD
=======
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
        
        if event.key == pygame.K_ESCAPE:
            setattr(self.engine, "quit_flag", True)

    def _advance(self):
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
        # ... (tu código _advance está bien) ...
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
        if self._line_index < len(self.lines) - 1:
=======
        # Advance to the next line or show choices
        if self._line_index < len(self.lines):
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        self.apply_effects(choice.get("effects", []))
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======

    # ¡DELEGA! El motor sabe cómo manejar los efectos.
        self.engine.apply_effects(choice.get("effects", [])) 

>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
=======
        self.engine.apply_effects(choice.get("effects", [])) 
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======

        # Play choice SFX (if any)
        sfx = choice.get("sfx")
        if sfx:
            self.engine.play_sound(sfx)

        # Apply choice effects
        self.engine.apply_effects(choice.get("effects", [])) 
        
        # Load target scene
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
        target = choice.get("target") or choice.get("next") or choice.get("scene")
        if target:
            self.engine.scene_manager.load_scene(target)

<<<<<<< HEAD
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

=======
>>>>>>> 8530cab ( implement transition manager and refactor scene loading with image caching)
    def update(self, dt):
        # Update chapter title (if any)
        if self.chapter_title:
            self.chapter_title.update(dt)

    def draw(self, surface):
<<<<<<< HEAD
<<<<<<< HEAD
        # Draw background, title, current dialog line, and choices.
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
        # 1. Fondo (Capa 0)
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
        # 1. Draw background 
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
        if self._bg_surf:
            surface.blit(self._bg_surf, (0, 0))
        else:
            surface.fill((0, 0, 0))
<<<<<<< HEAD
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
=======
        
<<<<<<< HEAD
        # (Capa 1 - Actores/Animaciones: El AnimationManager lo dibuja automáticamente)
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
        # HERE I WILL CREATE ANIMATION_MANAGER TO HANDLE ANIMATED BACKGROUNDS LATER
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)

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
<<<<<<< HEAD
        # True when at last line and choices exist
<<<<<<< HEAD
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
=======
        return self._line_index >= max(0, len(self.lines) - 1) and bool(self.choices)
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
        # Returns True if we are at the end of lines and have choices to show
        return self._line_index == len(self.lines) and bool(self.choices)
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
=======
# scene.py
=======
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
# scene.py
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
import pygame
from ui import DialogueBox, ChapterTitle

class Scene:
    def __init__(self, engine, data=None):
        # Store references and initialize runtime state
        self.engine = engine
        self.data = data or {}
        self.id = self.data.get("id", "unnamed")

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
        if self.background:
            try:
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

<<<<<<< HEAD
<<<<<<< HEAD
        # optional music control via engine
        music = self.data.get("music")
        if music and hasattr(self.engine, "play_music"):
            try:
                self.engine.play_music(music)
            except Exception:
                pass
<<<<<<< HEAD
        pass
>>>>>>> b4d0ed7 (Run and debug)
=======

=======
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
    def exit(self):
        # Placeholder for cleanup when a scene is replaced
        return
=======
    def exit(self): 
        return # Placeholder for cleanup when a scene is replaced
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)

    def handle_event(self, event):
        # If there is a chapter title being shown, block input until it finishes
        if self.chapter_title and not self.chapter_title.is_finished():
             return 

        # Handle keydown events for dialogue progression and choices
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
        target = choice.get("target") or choice.get("next") or choice.get("scene")
        if target:
            self.engine.scene_manager.load_scene(target)

    def update(self, dt):
        # Update chapter title (if any)
        if self.chapter_title:
            self.chapter_title.update(dt)

    def draw(self, surface):
        # 1. Draw background 
        if self._bg_surf:
            surface.blit(self._bg_surf, (0, 0))
        else:
            surface.fill((0, 0, 0))
        
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
<<<<<<< HEAD
        # True when at last line and choices exist
<<<<<<< HEAD
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
=======
        return self._line_index >= max(0, len(self.lines) - 1) and bool(self.choices)
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
        # Returns True if we are at the end of lines and have choices to show
        return self._line_index == len(self.lines) and bool(self.choices)
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
=======
# scene.py
=======
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
=======
# scene.py
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
import pygame
from ui import DialogueBox, ChapterTitle

class Scene:
    def __init__(self, engine, data=None):
        # Store references and initialize runtime state
        self.engine = engine
        self.data = data or {}
        self.id = self.data.get("id", "unnamed")

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
        if self.background:
            try:
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

<<<<<<< HEAD
<<<<<<< HEAD
        # optional music control via engine
        music = self.data.get("music")
        if music and hasattr(self.engine, "play_music"):
            try:
                self.engine.play_music(music)
            except Exception:
                pass
<<<<<<< HEAD
        pass
>>>>>>> b4d0ed7 (Run and debug)
=======

=======
>>>>>>> c402bd6 (refactor: improve code readability with comments and remove unused file)
    def exit(self):
        # Placeholder for cleanup when a scene is replaced
        return
=======
    def exit(self): 
        return # Placeholder for cleanup when a scene is replaced
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)

    def handle_event(self, event):
        # If there is a chapter title being shown, block input until it finishes
        if self.chapter_title and not self.chapter_title.is_finished():
             return 

        # Handle keydown events for dialogue progression and choices
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
        target = choice.get("target") or choice.get("next") or choice.get("scene")
        if target:
            self.engine.scene_manager.load_scene(target)

    def update(self, dt):
        # Update chapter title (if any)
        if self.chapter_title:
            self.chapter_title.update(dt)

    def draw(self, surface):
        # 1. Draw background 
        if self._bg_surf:
            surface.blit(self._bg_surf, (0, 0))
        else:
            surface.fill((0, 0, 0))
        
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
<<<<<<< HEAD
        # True when at last line and choices exist
<<<<<<< HEAD
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
=======
        return self._line_index >= max(0, len(self.lines) - 1) and bool(self.choices)
>>>>>>> a910009 (improve scene management and UI integration in scene.py; fix DialogueBox class for better text rendering in ui.py)
=======
        # Returns True if we are at the end of lines and have choices to show
        return self._line_index == len(self.lines) and bool(self.choices)
>>>>>>> 61b4333 (Perform a code debug by adding music and editing the data-driven files, as well as the scene and engine files.)
=======
# scene.py
=======
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
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
<<<<<<< HEAD
        pass
>>>>>>> b4d0ed7 (Run and debug)
=======

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
        # Title: centered at the top of the screen
        if title and self.title_font:
            surf = self.title_font.render(title, True, (255, 255, 255))
            rect = surf.get_rect()
            rect.centerx = surface.get_width() // 2
            rect.y = 20
            surface.blit(surf, rect)

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
                txt_rect = txt_surf.get_rect()
                txt_rect.centerx = surface.get_width() // 2
                # place the line ~60px above the bottom edge
                txt_rect.y = surface.get_height() - 60 - txt_rect.height // 2
                surface.blit(txt_surf, txt_rect)

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
>>>>>>> d07fceb (Create def draw in the scene file to load data driven)
