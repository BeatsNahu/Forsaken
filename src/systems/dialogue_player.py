import pygame
from systems.ui_components import DialogueBox

class DialoguePlayer:
    """
    Gestiona la lógica de mostrar una lista de líneas de diálogo
    una tras otra. Es un "reproductor" de diálogo autocontenido.
    """
    def __init__(self, engine, lines_list: list):
        self.engine = engine
        self.lines = lines_list
        self._line_index = 0
        
        # Cada reproductor crea su propia instancia de DialogueBox
        self.ui = DialogueBox(self.engine)
        self.ui.fade_in()
        
        self.state = "TYPING" # "TYPING" o "FINISHED"
        
        # Sonidos (¡Esto es un avance contra el hardcoding!)
        # Podríamos cargar esto desde un config.
        self.sfx_advance = "assets/audio/sfx/type_writing1.ogg"
        self.sfx_skip = "assets/audio/sfx/type_writing1.ogg" # O un sonido diferente

    def handle_event(self, event):
        """Gestiona el input para avanzar el diálogo."""
        if event.type != pygame.KEYDOWN:
            return
            
        if self.state == "TYPING" and event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
            if not self.ui.is_finished():
                # Si está escribiendo, saltar al final
                self.ui.skip_typing()
                self.engine.play_sound(self.sfx_skip, volume=0.5)
            else:
                # Si ya terminó, avanzar a la siguiente línea
                self.engine.play_sound(self.sfx_advance, volume=0.5)
                self._advance()

    def _advance(self):
        """Pasa a la siguiente línea de diálogo."""
        self._line_index += 1
        
        # Comprobar si se acabaron las líneas
        if self._line_index >= len(self.lines):
            self.state = "FINISHED"
            self.ui.fade_out()
            return
            
        # Si la nueva línea tiene un SFX, reproducirlo
        line_data = self.lines[self._line_index]
        if isinstance(line_data, dict):
            sfx = line_data.get("sfx")
            if sfx:
                self.engine.play_sound(sfx)

    def update(self, dt):
        """Actualiza la UI del diálogo."""
        # El UI se actualiza incluso si hemos terminado,
        # para gestionar su propio fade-out.
        self.ui.update(dt)

    def draw(self, surface):
        """Dibuja la caja de diálogo."""
        
        # Si terminamos, solo dibuja si está en fade-out
        if self.state == "FINISHED":
            if not self.ui.is_fade_complete():
                self.ui.draw(surface, text=None, speaker=None)
            return

        # Si estamos escribiendo, coge la línea actual
        line_data = {}
        if self._line_index < len(self.lines):
            line_data = self.lines[self._line_index]
        
        text = line_data.get("text", "")
        speaker = line_data.get("speaker")
        
        self.ui.draw(surface, text=text, speaker=speaker)
            
    def is_finished(self) -> bool:
        """
        Devuelve True solo cuando el diálogo ha terminado Y
        la animación de fade-out de la UI se ha completado.
        """
        return self.state == "FINISHED" and self.ui.is_fade_complete()