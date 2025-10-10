# scene.py
class Scene:
    def __init__(self, engine, data=None):
        self.engine = engine
        self.data = data or {}
        self.id = self.data.get("id", "unnamed")
        self.background = self.data.get("background")
        self.lines = self.data.get("lines", [])
        self.choices = self.data.get("choices", [])
        self._line_index = 0

    def enter(self): pass
    def exit(self): pass

    def handle_event(self, event):
        # avance por defecto con Enter
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
            self._advance()

    def _advance(self):
        if self._line_index < len(self.lines)-1:
            self._line_index += 1
        else:
            if self.choices:
                # abrir UI para elegir (delegar a engine.ui o implementar directo)
                pass
            elif "next" in self.data:
                self.apply_effects(self.data.get("effects", []))
                self.engine.scene_manager.load_scene(self.data["next"])

    def apply_effects(self, effects):
        for e in effects:
            if e.get("type") == "give_item":
                self.engine.add_item(e["item"])
            elif e.get("type") == "set_var":
                self.engine.set_var(e["name"], e["value"])
            elif e.get("type") == "start_battle":
                self.engine.scene_manager.load_scene(e["battle_module"])

    def update(self, dt): pass
    def draw(self, surface): 
        # dibujar background y texto actual
        pass
