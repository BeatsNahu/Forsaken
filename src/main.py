import pygame
from engine import Engine
from scene_manager import SceneManager
from scene import Scene

def main():
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption("Forsaken")
    clock = pygame.time.Clock()

    engine = Engine()
    engine.screen = screen
    engine.clock = clock

    escene_manager = SceneManager(engine, Scene)
    engine.scene_manager = escene_manager

    escene_manager.load_scene("src.scripts.menu") # Load the menu scene


    running = True
    # Main loop
    while running and not getattr(engine, "quit_flag", False):
        dt = clock.tick(60) / 1000.0  # Delta time in seconds
        for event in pygame.event.get(): # Event handling loop
            if event.type == pygame.QUIT:
                running = False
                break  
            SceneManager.handle_event(event) # Handle other events like keyboard
            
        # Update game state
        SceneManager.update(dt)

        # Screen rendering
        SceneManager.draw(screen)
        pygame.display.flip() # Display the updated screen

        # Control frame rate

    # Finalize
    pygame.quit()

if __name__ == "__main__":
    main()