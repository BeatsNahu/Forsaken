import pygame

class AnimationManager:
    def __init__(self, engine):
        self.engine = engine
        self.animations = [
            "slide_in",
            "slide_out",
            "zoom_in",
            "zoom_out"
        ]
        self.screen = engine.screen
    
    def slide_in(self, target_pos, duration=1000):
        pass
    def slide_out(self, target_pos, duration=1000):
        pass

    def zoom_in(self, scale_factor, duration=1000):
        pass
    def zoom_out(self, scale_factor, duration=1000):
        pass    
    def play_animation(self, animation_name, duration=1000):
        pass