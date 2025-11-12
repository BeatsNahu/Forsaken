from systems.tween import Tween

class AnimationManager:
    def __init__(self, engine):
        self.engine = engine
        self.active_tweens = {} # Store active tweens by their IDs
        self._next_id = 0

    def _generate_id(self):
        self._next_id += 1
        return f"__tween_{self._next_id}"

    def start_animation(self, surface, start_pos, end_pos, duration, id=None, start_scale=1.0, end_scale=1.0, persist=False):
        if id is None:
            id = self._generate_id()
            
        tween = Tween(
            surface, 
            start_pos, 
            end_pos, 
            duration, 
            id, 
            start_scale, 
            end_scale, 
            persist,
        )
        self.active_tweens[id] = tween
        print(f"[AnimManager] Iniciando animación: {id}")
        return id

    def stop_animation(self, id):
        if id in self.active_tweens:
            del self.active_tweens[id]

    def is_animating(self, id):
        return id in self.active_tweens

    def update(self, dt):
        # Iterate over a copy so that we can safely delete
        for id in list(self.active_tweens.keys()):
            tween = self.active_tweens[id]
            tween.update(dt)

            if tween.is_finished and not tween.persist:
                del self.active_tweens[id]
                
    def draw(self, surface):
        for tween in self.active_tweens.values():
            tween.draw(surface)