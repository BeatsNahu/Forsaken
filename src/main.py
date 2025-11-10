import pygame
from core.engine import Engine                 
from core.scene_manager import SceneManager    
from core.scene import Scene                   
from systems.transition_manager import TransitionManager 
from systems.battle_manager import BattleManager

def main():
    # Screen setup
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Forsaken")
    icono = pygame.image.load("assets/ui/logo.png")
    pygame.display.set_icon(icono)
    logo = pygame.transform.scale(icono, (96, 96))
    clock = pygame.time.Clock()

    # With this part we avoid repeated code in every scene, because all scenes will have access to the screen and clock initialized in "Screen setup"
    engine = Engine() # Create an instance of the Engine
    engine.screen = screen # Assign the screen to the engine
    engine.clock = clock # Assign the clock to the engine
    # Now that the engine has a screen, create the TransitionManager which needs screen size
    engine.transition_manager = TransitionManager(engine)

    # Dictionary of scene classes available in the game
    scene_classes = {
        "default": Scene,
        "BattleManager": BattleManager,
    }

    escene_manager = SceneManager(engine, scene_classes) # Create an instance of the SceneManager using the Engine and Scene classes
    engine.scene_manager = escene_manager # Assign the scene manager to the engine 
    
    escene_manager.load_scene("scenes.main_menu") # Load the main menu scene
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
        escene_manager.draw(screen) # The draw method of the scene manager will call the draw method of the current scene
        pygame.display.flip() # Display the updated screen
    # Finalize
    pygame.quit()

if __name__ == "__main__": # If this script is run directly the game will start
    main()