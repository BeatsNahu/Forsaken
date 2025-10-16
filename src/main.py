import pygame
from engine import Engine
from scene_manager import SceneManager
from scene import Scene


def main():
    # Screen setup
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Forsaken")
    clock = pygame.time.Clock()

    # With this part we avoid repeated code in every scene, because all scenes will have access to the screen and clock initialized in "Screen setup"
    engine = Engine() # Create an instance of the Engine
    engine.screen = screen # Assign the screen to the engine
    engine.clock = clock # Assign the clock to the engine

    escene_manager = SceneManager(engine, Scene) # Create an instance of the SceneManager using the Engine and Scene classes
    engine.scene_manager = escene_manager # Assign the scene manager to the engine 
    
    escene_manager.load_scene("scripts.main_menu") # Load the main menu scene
    # Main game loop
    dt = clock.tick(60) / 1000.0  # Delta time is used to make the game frame rate independent of the cpu speed, with this we can make the game run at the same speed on different computers
    running = True
<<<<<<< HEAD
    # Main loop
<<<<<<< HEAD
    while running:
<<<<<<< HEAD
        for event in pygame.event.get():
<<<<<<< HEAD
<<<<<<< HEAD
            if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked the x
                running = False # So the loop will stop running and finish the game
            game.handle_event(event) # Handle other events like keyboard
            
        # Update game state
        game.update() 
=======
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)
            
        # Update game state
        game.update()
>>>>>>> 4520943 (I created the initial game configuration)
=======
            if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked the x
                running = False # So the loop will stop running and finish the game
            game.handle_event(event) # Handle other events like keyboard
            
        # Update game state
        game.update() 
>>>>>>> b6088aa (Merge)

        # Screen rendering
        screen.fill((0, 0, 0))
        game.draw(screen)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
    while running and not getattr(engine, "quit_flag", False):
        dt = clock.tick(60) / 1000.0  # Delta time in seconds
>>>>>>> e6242d4 (Completion of main.py and editing the menu.py file)
        for event in pygame.event.get(): # Event handling loop
            if event.type == pygame.QUIT:
                running = False
                break  
            SceneManager.handle_event(event) # Handle other events like keyboard
=======
    while running and not getattr(engine, "quit_flag", False): # While running is True and the quit_flag is not set from any scene
        for event in pygame.event.get(): # In every second we have diferents events, so with this we are trying to get all the events
            if event.type == pygame.QUIT: # and if one is an event of type QUIT, we will stop the loop
                running = False # Running is set to False and the loop will 
                break  # Exit the event loop
<<<<<<< HEAD
<<<<<<< HEAD
        SceneManager.handle_event(event) # Handle other events like keyboard
>>>>>>> 32ed7b6 (Edition and comments of main.py)
=======
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
            
=======

        escene_manager.handle_event(event) # The handle_event method of the scene manager will call the handle_event method of the current scene, passing the event as argument

>>>>>>> 59da024 (Finish the window menu, we need to can select one option and swap the scene or exit the game)
        # Update game state
        escene_manager.update(dt) # The update method of the scene manager will call the update method of the current scene, passing the delta time as argument

        # Screen rendering
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        screen.fill((0, 0, 0))
        Engine.draw(screen)
>>>>>>> 9dd9a3f (Editing the main - engine - escene_maganer files and configuring them and eliminating extra files. I'm trying to do the first escene)
=======
        SceneManager.draw(screen)
>>>>>>> e6242d4 (Completion of main.py and editing the menu.py file)
=======
        SceneManager.draw(screen) # The draw method of the scene manager will call the draw method of the current scene
>>>>>>> 32ed7b6 (Edition and comments of main.py)
=======
        escene_manager.draw(screen) # The draw method of the scene manager will call the draw method of the current scene
>>>>>>> 5b2e0a0 (Main.py - scene:manager and main_menu are working)
        pygame.display.flip() # Display the updated screen
=======
        pygame.display.flip()
>>>>>>> 4520943 (I created the initial game configuration)
=======
        pygame.display.flip() # Display the updated screen
>>>>>>> b6088aa (Merge)

        # Control frame rate

    # Finalize
    pygame.quit()

if __name__ == "__main__":
    main()