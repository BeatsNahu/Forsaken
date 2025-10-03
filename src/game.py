import pygame
from player import Player

class Game:
    def __init__(self):
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            self.player.handle_event(event)

    def update(self):
        self.all_sprites.update()

    def draw(self, screen):
        self.all_sprites.draw(screen)