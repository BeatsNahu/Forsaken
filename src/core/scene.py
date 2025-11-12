import pygame
from systems.ui_components import ChapterTitle, ChoiceBox
from systems.dialogue_player import DialoguePlayer
import config
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

        # Cached surfaces
        self._bg_surf = None
        self.pending_target = None 

        # Machine of states
        self.state = "START"
        
        # Runtime UI components 
        self.chapter_title = None
        self._dialogue_player = None
        self._choice_box = None

        # Chapter title component (if any)
        ui_sounds = self.data.get("ui_sounds", {})
        self._sfx_confirm = ui_sounds.get("confirm_choice", config.SFX_UI_CONFIRM)

    def enter(self):
        # Load background image
        self._bg_surf = None
        if self.background:
            try:
                surf = self.engine.load_image(self.background)
                if surf:
                    self._bg_surf = pygame.transform.scale(surf, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
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
            persist_val = anim_data.get("persist", False)
            
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
                persist=persist_val
            )
        # 4. Aplicar efectos al entrar
        self.engine.apply_effects(self.data.get("effects_on_enter", []))

        # 6. Set initial state for chapter title or dialogue box
        if self.data.get("title"):
            self.state = "TITLE"
            self.chapter_title = ChapterTitle(self.engine, self.data.get("title"))
        elif self.lines:
            # Si no hay título pero hay líneas, empezamos el diálogo
            self.state = "DIALOGUE"
            self._dialogue_player = DialoguePlayer(self.engine, self.lines)
        elif self.choices:
            # Si no hay líneas pero sí choices
            self.state = "CHOICES"
            self._choice_box = ChoiceBox(self.engine, self.choices, self.data.get("choice_config"))
            self._choice_box.fade_in()
        else:
            # Escena vacía
            self.state = "DONE"

    def exit(self): 
        return # Placeholder for cleanup when a scene is replaced

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        
        if self.state == "DIALOGUE" and self._dialogue_player:
            # Le pasamos el evento al reproductor de diálogo
            self._dialogue_player.handle_event(event)

        elif self.state == "CHOICES" and self._choice_box:
            # 1. Eventos internos del ChoiceBox (Arriba/Abajo)
            self._choice_box.handle_event(event)
            
            # 2. Evento de confirmar (Enter)
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self.engine.play_sound(self._sfx_confirm)
                choice_data = self._choice_box.get_selected_choice()
                self._choose(choice_data)

    def _choose(self, choice_data):
        """Lógica que se ejecuta al confirmar una opción."""
        if not choice_data: return
        
        # 1. Aplicar efectos
        self.engine.apply_effects(choice_data.get("effects", [])) 

        # 2. Decidir qué hacer (líneas post-choice o cambiar escena)
        post_lines = choice_data.get("post_choice_lines")
        target = choice_data.get("target")

        if post_lines:
            # Si hay líneas, volvemos al estado de Diálogo
            self.lines = post_lines
            self.choices = None # Ya no hay choices
            self.pending_target = target # Guardamos el destino para *después*
            
            self.state = "DIALOGUE"
            self._dialogue_player = DialoguePlayer(self.engine, self.lines)
            self._choice_box = None # Destruimos el choice box
        
        elif target:
            # Si no hay líneas, cargamos la escena
            self.state = "DONE"
            self.engine.scene_manager.load_scene(target)
        
    def update(self, dt):
        if self.state == "TITLE":
            self.chapter_title.update(dt)
            if self.chapter_title.is_finished():
                # Título terminado, pasamos a Diálogo (si hay)
                if self.lines:
                    self.state = "DIALOGUE"
                    self._dialogue_player = DialoguePlayer(self.engine, self.lines)
                    self.chapter_title = None
                elif self.choices:
                    self.state = "CHOICES"
                    self._choice_box = ChoiceBox(self.engine, self.choices, self.data.get("choice_config"))
                    self._choice_box.fade_in()
                else:
                    self.state = "DONE"

        elif self.state == "DIALOGUE":
            if not self._dialogue_player: return # Seguridad
            
            self._dialogue_player.update(dt)
            if self._dialogue_player.is_finished():
                self._dialogue_player = None # Destruimos el reproductor
                
                # Diálogo terminado. ¿Qué sigue?
                if self.choices:
                    # Siguen las choices
                    self.state = "CHOICES"
                    self._choice_box = ChoiceBox(self.engine, self.choices, self.data.get("choice_config"))
                    self._choice_box.fade_in()
                elif self.pending_target:
                    # (Viene de un post_choice_lines)
                    self.state = "DONE"
                    self.engine.scene_manager.load_scene(self.pending_target)
                elif self.data.get("next"):
                    # (Es el final de la escena)
                    self.state = "DONE"
                    self.engine.scene_manager.load_scene(self.data["next"])
                else:
                    self.state = "DONE" # No hay nada más

        elif self.state == "CHOICES":
            if self._choice_box:
                self._choice_box.update(dt)

        elif self.state == "DONE":
            # No hacer nada, esperando cambio de escena
            pass

    def draw(self, surface):
        # 1. Draw background 
        if self._bg_surf:
            surface.blit(self._bg_surf, (0, 0))
        else:
            surface.fill((0, 0, 0))

        # 2. Draw chapter title
        if self.state == "TITLE":
            self.chapter_title.draw(surface)
        
        # 3. Draw UI elements
        if self._dialogue_player:
            self._dialogue_player.draw(surface)
            
        if self._choice_box:
            self._choice_box.draw(surface)