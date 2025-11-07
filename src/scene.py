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

    def exit(self): 
        return # Placeholder for cleanup when a scene is replaced

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
                # Check if text is still being typed
                if not self.ui.is_finished():
                    # If still typing -> skip to full text
                    self.ui.skip_typing()
                else:
                    # If text fully displayed -> advance to next line
                    self.engine.play_sound("assets/sfx/dialogue_next.ogg")
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
        # Update chapter title and UI components 
        if self.chapter_title:
            self.chapter_title.update(dt)

        if self.ui:
            self.ui.update(dt)

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
        # Returns True if we are at the end of lines and have choices to show
        return self._line_index == len(self.lines) and bool(self.choices)