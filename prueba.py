import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Forsaken")
clock = pygame.time.Clock()

test_font = pygame.font.Font("assets/fonts/Pixeltype.ttf", 50)

jail_surface = pygame.image.load("assets/backgrounds/Jail.png").convert()
jail_surface = pygame.transform.scale(jail_surface, (1920, 1080))

evilbob = pygame.image.load("assets/characters/Evil_bob1.png").convert_alpha()
evilbob = pygame.transform.scale(evilbob, (576, 576))
evilbob_x_pos = -100

text_surface = test_font.render("Hello World", False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(jail_surface,(0, 0))
    
    evilbob_x_pos += 50
    if evilbob_x_pos >= 600:
        evilbob_x_pos = 600

    screen.blit(evilbob,(evilbob_x_pos, 160))
    screen.blit(text_surface,(800, 100))
    
    pygame.display.update()
    clock.tick(60)