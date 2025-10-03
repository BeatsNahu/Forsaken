import pygame
<<<<<<< HEAD
from engine import Engine
from scene_manager import SceneManager
from scene import Scene
<<<<<<< HEAD
<<<<<<< HEAD
from transition_manager import TransitionManager

=======
>>>>>>> 5a11d94 (Completion of main.py and editing the menu.py file)
=======
from transition_manager import TransitionManager
>>>>>>> be8071d ( implement transition manager and refactor scene loading with image caching)


def main():
    # Screen setup
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Forsaken")
    icono = pygame.image.load("assets/button/logo.png")
    pygame.display.set_icon(icono)
    logo = pygame.transform.scale(icono, (96, 96))
    clock = pygame.time.Clock()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 142a39d (Finish the window menu, we need to can select one option and swap the scene or exit the game)
    # With this part we avoid repeated code in every scene, because all scenes will have access to the screen and clock initialized in "Screen setup"
    engine = Engine() # Create an instance of the Engine
    engine.screen = screen # Assign the screen to the engine
    engine.clock = clock # Assign the clock to the engine
    # Now that the engine has a screen, create the TransitionManager which needs screen size
    engine.transition_manager = TransitionManager(engine)
<<<<<<< HEAD

    escene_manager = SceneManager(engine, Scene) # Create an instance of the SceneManager using the Engine and Scene classes
    engine.scene_manager = escene_manager # Assign the scene manager to the engine 
    
    escene_manager.load_scene("scripts.main_menu") # Load the main menu scene
    # Main game loop
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
=======
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
<<<<<<< HEAD
>>>>>>> 4520943 (I created the initial game configuration)
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)
            
        # Update game state
        game.update()
<<<<<<< HEAD
>>>>>>> 4520943 (I created the initial game configuration)
=======
            if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked the x
                running = False # So the loop will stop running and finish the game
            game.handle_event(event) # Handle other events like keyboard
            
        # Update game state
        game.update() 
>>>>>>> b6088aa (Merge)
=======
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
<<<<<<< HEAD
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
=======
        # Process all events and forward each one to the current scene
        for event in pygame.event.get(): # collect events
            if event.type == pygame.QUIT:
                running = False
                break
            escene_manager.handle_event(event) # forward every event immediately to the scene manager
>>>>>>> 09fc689 (the menu has been repaired and scenes started to be created)

        # Delta time should be computed once per frame, after processing events
        dt = clock.tick(60) / 1000.0  # Delta time is used to make the game frame rate independent of the cpu speed

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
=======
    engine = Engine()
    engine.screen = screen
    engine.clock = clock
=======
    # Wtih this part we avoid repeated code in every scene, because all scenes will have access to the escreen and clock initialized in "Screen setup"
=======
    # With this part we avoid repeated code in every scene, because all scenes will have access to the escreen and clock initialized in "Screen setup"
>>>>>>> 4fa55ba (Main.py - scene:manager and main_menu are working)
    engine = Engine() # Create an instance of the Engine
    engine.screen = screen # Assign the screen to the engine
    engine.clock = clock # Assign the clock to the engine
>>>>>>> 17a30bb (Edition and comments of main.py)
=======
>>>>>>> be8071d ( implement transition manager and refactor scene loading with image caching)

    escene_manager = SceneManager(engine, Scene) # Create an instance of the SceneManager using the Engine and Scene classes
    engine.scene_manager = escene_manager # Assign the scene manager to the engine 
    
    escene_manager.load_scene("scripts.main_menu") # Load the main menu scene
    # Main game loop
    running = True
    while running and not getattr(engine, "quit_flag", False): # While running is True and the quit_flag is not set from any scene
        # Process all events and forward each one to the current scene
        for event in pygame.event.get(): # collect events
            if event.type == pygame.QUIT:
                running = False
                break
            escene_manager.handle_event(event) # forward every event immediately to the scene manager

        # Delta time should be computed once per frame, after processing events
        dt = clock.tick(60) / 1000.0  # Delta time is used to make the game frame rate independent of the cpu speed

        # Update game state
        escene_manager.update(dt) # The update method of the scene manager will call the update method of the current scene, passing the delta time as argument

        # Screen rendering
<<<<<<< HEAD
<<<<<<< HEAD
        SceneManager.draw(screen)
>>>>>>> 5a11d94 (Completion of main.py and editing the menu.py file)
=======
        SceneManager.draw(screen) # The draw method of the scene manager will call the draw method of the current scene
>>>>>>> 17a30bb (Edition and comments of main.py)
=======
        escene_manager.draw(screen) # The draw method of the scene manager will call the draw method of the current scene
>>>>>>> 4fa55ba (Main.py - scene:manager and main_menu are working)
        pygame.display.flip() # Display the updated screen
<<<<<<< HEAD
<<<<<<< HEAD
=======
        pygame.display.flip()
>>>>>>> 4520943 (I created the initial game configuration)
=======
        pygame.display.flip() # Display the updated screen
>>>>>>> b6088aa (Merge)

        # Control frame rate

=======
>>>>>>> 09fc689 (the menu has been repaired and scenes started to be created)
=======
>>>>>>> 163fdae (the menu has been repaired and scenes started to be created)
    # Finalize
    pygame.quit()

if __name__ == "__main__": # If this script is run directly the game will start
=======
        pygame.display.flip()
=======
        pygame.display.flip() # Display the updated screen
>>>>>>> b6088aa (Merge)

        # Control frame rate
        clock.tick(60)

    # Finalize
    pygame.quit()

if __name__ == "__main__":
>>>>>>> 4520943 (I created the initial game configuration)
    main()