import pygame
from engine import Engine
from scene_manager import SceneManager
from scene import Scene

def main():
    # Screen setup
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption("Forsaken")
    clock = pygame.time.Clock()

    # Wtih this part we avoid repeated code in every scene, because all scenes will have access to the escreen and clock initialized in "Screen setup"
    engine = Engine() # Create an instance of the Engine
    engine.screen = screen # Assign the screen to the engine
    engine.clock = clock # Assign the clock to the engine

    escene_manager = SceneManager(engine, Scene) # Create an instance of the SceneManager using the Engine and Scene classes
    engine.scene_manager = escene_manager # Assign the scene manager to the engine 

    escene_manager.load_scene("scripts.menu") # Load the initial scene, in this case the menu scene

    # Main game loop
    running = True
    while running and not getattr(engine, "quit_flag", False): # While running is True and the quit_flag is not set from any scene
        dt = clock.tick(60) / 1000.0  # Delta time is used to make the game frame rate independent of the cpu speed, with this we can make the game run at the same speed on different computers
        for event in pygame.event.get(): # In every second we have diferents events, so with this we are trying to get all the events
            if event.type == pygame.QUIT: # and if one is an event of type QUIT, we will stop the loop
                running = False # Running is set to False and the loop will 
                break  # Exit the event loop
        SceneManager.handle_event(event) # Handle other events like keyboard
            
        # Update game state
        SceneManager.update(dt)

        # Screen rendering
        SceneManager.draw(screen) # The draw method of the scene manager will call the draw method of the current scene
        pygame.display.flip() # Display the updated screen

        # Control frame rate

    # Finalize
    pygame.quit()

if __name__ == "__main__":
    main()