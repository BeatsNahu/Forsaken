import pygame
from systems.ui_manager import DialogueBox, ChapterTitle, ChoiceBox

class Scene:
    def __init__(self, engine, data=None):
        # Store references and initialize runtime state
        self.engine = engine
        self.data = data or {}
        self.id = self.data.get("id", "unnamed")

        # Scene content
        self.background = self.data.get("background")
        self.lines = self.data.get("lines", [])
        self.choices = self.data.get("choices")

        # Runtime indexes and cached surfaces
        self._line_index = 0
        self._choice_index = 0
        self._bg_surf = None
        self.pending_target = None

        # Runtime UI components 
        self.ui = DialogueBox(self.engine)
        self.choice_ui = ChoiceBox(self.engine)

        # Chapter title component (if any)
        self.chapter_title = None
        if self.data.get("title"):
            self.chapter_title = ChapterTitle(self.engine, self.data.get("title"))

        # Machine of states
        self.state = "START"
        if self.chapter_title:
            self.state = "TITLE" # Start showing chapter title first
        else:
            self.state = "FADE_IN_DIALOGUE" # Directly fade in dialogue box

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

        # 3. Animation 
        anim_data_list = self.data.get("animations_on_enter", [])
        
        for anim_data in anim_data_list:
            # 1. Load image for animation
            img_surf = self.engine.load_image(anim_data.get("image"))
            if not img_surf: continue
                
            # 2. Call AnimationManager to start the animation
            persist_val = anim_data.get("persist", anim_data.get("persisting", False))
            
            self.engine.animation_manager.start_animation(
                surface=img_surf,
                id=anim_data.get("id"),

                # Slide
                start_pos=anim_data.get("start_pos", [0,0]),
                end_pos=anim_data.get("end_pos", [0,0]),

                # Duration
                duration=anim_data.get("duration", 1.0),

                # Scale (zoom)
                start_scale=anim_data.get("start_scale", 1.0),
                end_scale=anim_data.get("end_scale", 1.0),

                # Persist after finishing
                persisting=persist_val
            )
        # 4. Aplicar efectos al entrar
        effects = self.data.get("effects_on_enter", [])
        self.engine.apply_effects(effects)

        # 5. Animation (tu código de animación)
        anim_data_list = self.data.get("animations_on_enter", [])

        # 6. Set initial state for chapter title or dialogue box
        if self.state == "FADE_IN_DIALOGUE":
            self.ui.fade_in()

    def exit(self): 
        return # Placeholder for cleanup when a scene is replaced

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_ESCAPE:
            setattr(self.engine, "quit_flag", True)
            return
        
        state = self.state
        if state == "TITLE":
            return
        
        elif state == "TYPING" or state == "POST_CHOICE_TYPING":
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                if not self.ui.is_finished():
                    self.ui.skip_typing()
                else:
                    self.engine.play_sound("assets/audio/sfx/type_writing1.ogg", volume=0.5)
                    self._advance()

        elif state == "CHOICES_VISIBLE":
            if event.key == pygame.K_DOWN:
                self._choice_index = (self._choice_index + 1) % max(1, len(self.choices))
                self.engine.play_sound("assets/audio/sfx/swap_option.ogg", volume=0.4)
            elif event.key == pygame.K_UP:
                self._choice_index = (self._choice_index - 1) % max(1, len(self.choices))
                self.engine.play_sound("assets/audio/sfx/swap_option.ogg", volume=0.4)
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self._choose(self._choice_index)
                self.engine.play_sound("assets/audio/sfx/option_selected.ogg", volume=0.4)

    def _advance(self):
        # Advance to the next line or show choices
        if self._line_index < len(self.lines) - 1:
            # Advance to next line
            self._line_index += 1
            if isinstance(self.lines[self._line_index], dict):
                sfx = self.lines[self._line_index].get("sfx")
                if sfx: self.engine.play_sound(sfx)
        else:
            # Fish line reached
            self._line_index += 1 # Move past the last line
            if self.choices:
                # Start faded choices
                self.state = "FADE_OUT_DIALOGUE"
                self.ui.fade_out()
                # Comprove "target"
            elif self.pending_target:
                self.engine.scene_manager.load_scene(self.pending_target)
            elif "next" in self.data:
                # If there are no choices, go to next scene if specified
                self.engine.apply_effects(self.data.get("effects", []))
                self.engine.scene_manager.load_scene(self.data["next"])

    def _choose(self, idx):
        if idx < 0 or idx >= len(self.choices):
            return
        
        choice = self.choices[idx]

        # Play choice SFX (if any) and at specified volume
        sfx = choice.get("sfx")
        volume = choice.get("sfx_volume", 1.0)
        if sfx:
            self.engine.play_sound(sfx, volume=volume)

        # Apply choice effects
        self.engine.apply_effects(choice.get("effects", [])) 

        # Post-Choice
        post_lines = choice.get("post_choice_lines")
        target = choice.get("target") or choice.get("next") or choice.get("scene")

        if post_lines:
            self.lines = post_lines         
            self._line_index = 0            
            self.pending_target = target    
            self.choices = None             
            self.state = "FADE_OUT_CHOICES" 
            self.choice_ui.fade_out()
        elif target:
            self.engine.scene_manager.load_scene(target)
        
    def update(self, dt):
        if self.state == "TITLE":
            if self.chapter_title:
                self.chapter_title.update(dt)
                if self.chapter_title.is_finished():
                    self.state = "FADE_IN_DIALOGUE"
                    self.ui.fade_in()
        
        elif self.state == "FADE_IN_DIALOGUE":
            self.ui.update(dt)
            if self.ui.is_fade_complete():
                self.state = "TYPING" 

        elif self.state == "TYPING":
            self.ui.update(dt)

        elif self.state == "POST_CHOICE_TYPING":
            self.ui.update(dt)

        elif self.state == "FADE_OUT_DIALOGUE":
            self.ui.update(dt)
            if self.ui.is_fade_complete():
                self.state = "FADE_IN_CHOICES"
                self.choice_ui.fade_in()
        
        elif self.state == "FADE_IN_CHOICES":
            self.choice_ui.update(dt)
            if self.choice_ui.is_fade_complete():
                self.state = "CHOICES_VISIBLE"

        elif self.state == "FADE_OUT_CHOICES":
            self.choice_ui.update(dt)
            if self.choice_ui.is_fade_complete():
                self.state = "FADE_IN_DIALOGUE"
                self.ui.fade_in()
            
        elif self.state == "CHOICES_VISIBLE":
            self.choice_ui.update(dt)

    def draw(self, surface):
        # 1. Draw background 
        if self._bg_surf:
            surface.blit(self._bg_surf, (0, 0))
        else:
            surface.fill((0, 0, 0))
        
        # HERE I WILL CREATE ANIMATION_MANAGER TO HANDLE ANIMATED BACKGROUNDS LATER

        # 2. Draw chapter title
        if self.state == "TITLE":
            if self.chapter_title:
                self.chapter_title.draw(surface)
        
        # 3. Draw UI elements
        else:
            ln = None
            if self._line_index < len(self.lines):
                ln = self.lines[self._line_index]
            
            text = ln.get("text", "") if isinstance(ln, dict) else (str(ln) if ln else None)
            speaker = ln.get("speaker") if isinstance(ln, dict) else None

            # Draw dialogue box or choices based on state
            if self.state in ["FADE_IN_DIALOGUE", "TYPING", "FADE_OUT_DIALOGUE", "POST_CHOICE_TYPING"]:
                self.ui.draw(surface, text=text, speaker=speaker)
            elif self.state in ["FADE_IN_CHOICES", "CHOICES_VISIBLE", "FADE_OUT_CHOICES"]:
                self.choice_ui.draw(surface, choices=self.choices, selected_idx=self._choice_index)
   
    def _is_showing_choices(self):
        # Returns True if we are at the end of lines and have choices to show
        return self.state == "CHOICES"