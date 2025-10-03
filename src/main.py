import pygame
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption("Forsaken")
    clock = pygame.time.Clock()
    running = True

    # Main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked the x
                running = False # So the loop will stop running and finish the game
            game.handle_event(event) # Handle other events like keyboard
            
        # Update game state
        game.update() 

        # Screen rendering
        screen.fill((0, 0, 0))
        game.draw(screen)
        pygame.display.flip() # Display the updated screen

        # Control frame rate
        clock.tick(60)

    # Finalize
    pygame.quit()

if __name__ == "__main__":
    main()