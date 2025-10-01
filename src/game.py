import pygame
from player import Player
<<<<<<< HEAD
import sys

class Game: # Create a Game class to manage game state
    def __init__(self): # Initialize game state 
        self.player = Player() # Create a player instance
        self.all_sprites = pygame.sprite.Group() # Group to hold all sprites
        self.all_sprites.add(self.player) # Add player to the sprite group


    def handle_event(self, event): # It means to handle events like keyboard input for the seleccion in the menu
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP: 
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif evento.key == pygame.K_UP:          # If the key is the Up Arrow
                print("Up") # It will print "Up"
            elif evento.key == pygame.K_DOWN:        # If the key is the Up Arrow
                print("Abajo") # It will print "Down"
            elif evento.key == pygame.K_KP_ENTER:    # If the key is Enter 
                print("Enter") # It will print "Enter"
            
            ### self.player.handle_event(event)
=======

class Game:
    def __init__(self):
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            self.player.handle_event(event)
>>>>>>> 4520943 (I created the initial game configuration)

    def update(self):
        self.all_sprites.update()

    def draw(self, screen):
        self.all_sprites.draw(screen)