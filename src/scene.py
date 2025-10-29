# scene.py
import pygame
import os
from ui import DialogueBox, ChapterTitle #

class Scene:
    def __init__(self, engine, data=None):
        # Store references and initialize runtime state
        self.engine = engine
        self.data = data or {}
        self.id = self.data.get("id", "unnamed")

        # scene content
        self.background = self.data.get("background")
        self.lines = self.data.get("lines", [])
        self.choices = self.data.get("choices") or self.data.get("choises") or []

        # runtime indexes and cached surfaces
        self._line_index = 0
        self._choice_index = 0
        self._bg_surf = None

        # --- ARREGLADO ---
        # Carga la UI que SÍ sabe dibujar texto
        self.ui = DialogueBox(self.engine) #

        # Chapter title component (if any)
        self.chapter_title = None
        if self.data.get("title"):
            self.chapter_title = ChapterTitle(self.engine, self.data.get("title")) #

    def enter(self):
        # --- ARREGLADO ---
        # Código de fondo limpiado. Eliminado el error de 'path'.
        self._bg_surf = None # Empezar como None
        if self.background:
            try:
                surf = self.engine.load_image(self.background)
                if surf:
                    self._bg_surf = pygame.transform.scale(surf, self.engine.screen.get_size())
            except Exception as e:
                print(f"Error al cargar fondo {self.background}: {e}")
                self._bg_surf = None
        
        # ¡YA NO SE CARGAN FUENTES AQUÍ! La UI lo hace.

    def exit(self):
        # Placeholder for cleanup when a scene is replaced
        return

    def handle_event(self, event):
        # Si el título se está mostrando, bloquear input
        if self.chapter_title and not self.chapter_title.is_finished(): #
             return 

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
        # ... (tu código _advance está bien) ...
        if self._line_index < len(self.lines) - 1:
            self._line_index += 1
            return
        if self.choices:
            self._choice_index = 0
            return
        if "next" in self.data:
            self.engine.apply_effects(self.data.get("effects", []))
            self.engine.scene_manager.load_scene(self.data["next"])

    def _choose(self, idx):
        # ... (tu código _choose está bien) ...
        if idx < 0 or idx >= len(self.choices):
            return
        choice = self.choices[idx]
        self.engine.apply_effects(choice.get("effects", [])) 
        target = choice.get("target") or choice.get("next") or choice.get("scene")
        if target:
            self.engine.scene_manager.load_scene(target)

    def update(self, dt):
        # Update chapter title (if any)
        if self.chapter_title:
            self.chapter_title.update(dt) #

    def draw(self, surface):
        # 1. Fondo (Capa 0)
        if self._bg_surf:
            surface.blit(self._bg_surf, (0, 0))
        else:
            surface.fill((0, 0, 0))
        
        # (Capa 1 - Actores/Animaciones: El AnimationManager lo dibuja automáticamente)

        # --- ARREGLADO ---
        # 2. Delegar el dibujado a la UI
        # La UI decidirá si dibujar elecciones o texto
        
        if self._is_showing_choices():
            # Le pasamos las elecciones a la UI
            self.ui.draw(surface, text=None, choices=self.choices, choice_idx=self._choice_index) #
        
        elif self.lines:
            # Conseguimos los datos de la línea actual
            ln = self.lines[self._line_index]
            text = ln.get("text", "") if isinstance(ln, dict) else str(ln)
            speaker = ln.get("speaker") if isinstance(ln, dict) else None
            
            # Le pasamos el texto y el hablante a la UI
            self.ui.draw(surface, text=text, speaker=speaker) #

        # 3. Dibujar Título (Capa 3 - Encima de todo)
        if self.chapter_title:
            self.chapter_title.draw(surface) #

    
    def _is_showing_choices(self):
        # True when at last line and choices exist
        return self._line_index >= max(0, len(self.lines) - 1) and bool(self.choices)