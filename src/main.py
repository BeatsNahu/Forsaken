import pygame
from engine import Engine
from scene_manager import SceneManager

def main():
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption("Forsaken")
    clock = pygame.time.Clock()
    running = True

    # Main loop
    while running:
        for event in pygame.event.get(): # Event handling loop
            Engine.handle_event(event) # Handle other events like keyboard
            
        # Update game state
        Engine.update() 

        # Screen rendering
        screen.fill((0, 0, 0))
        Engine.draw(screen)
        pygame.display.flip() # Display the updated screen

        # Control frame rate
        clock.tick(60)

    # Finalize
    pygame.quit()

if __name__ == "__main__":
    main()