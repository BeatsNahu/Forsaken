import pygame
import config
from core.engine import Engine                 
from core.scene_manager import SceneManager    
from core.scene import Scene                   
from systems.transition_manager import TransitionManager
from systems.animation_manager import AnimationManager
from systems.battle_manager import BattleManager
from overlays.pause_menu import PauseMenu


def main():
    # Screen setup
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption(config.GAME_TITLE)

    icono = pygame.image.load(config.GAME_ICON_PATH)
    pygame.display.set_icon(icono)

    clock = pygame.time.Clock()

    # With this part we avoid repeated code in every scene, because all scenes will have access to the screen and clock initialized in "Screen setup"
    engine = Engine() # Create an instance of the Engine
    engine.screen = screen # Assign the screen to the engine
    engine.clock = clock # Assign the clock to the engine
    # Now that the engine has a screen, create the TransitionManager which needs screen size
    engine.transition_manager = TransitionManager(engine)
    engine.animation_manager = AnimationManager(engine)

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
        # Event processing
        events = pygame.event.get()
        top_overlay = engine.get_top_overlay()
        # Process all events and forward each one to the current scene
        for event in events: # collect events
            if event.type == pygame.QUIT:
                running = False
                break
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if top_overlay:
                # If there is an overlay, ESC closes it
                    engine.pop_overlay()
                else:
                    # If there is no overlay, ESC opens the pause menu
                    # (Don't open it in the main menu!)
                    if engine.scene_manager.current_scene.id != "menu":
                        engine.push_overlay(PauseMenu(engine))
                continue # The ESC event has been handled

            if top_overlay:
                # If the top overlay has an event handler, forward the event to it
                if hasattr(top_overlay, "handle_event"):
                    top_overlay.handle_event(event)
            else:
                escene_manager.handle_event(event) # forward every event immediately to the scene manager
        
        if not running:
            break
    
        # Delta time should be computed once per frame, after processing events
        dt = clock.tick(config.FPS) / 1000.0  # Delta time is used to make the game frame rate independent of the cpu speed

        # Update game state
        if top_overlay:
            engine.update_overlays(dt)
        else:
            escene_manager.update(dt) # The update method of the scene manager will call the update method of the current scene, passing the delta time as argument

        # Screen rendering
        engine.transition_manager.update(dt)
        engine.animation_manager.update(dt)
        engine._update_notifications(dt)

        escene_manager.draw(screen) # The draw method of the scene manager will call the draw method of the current scene
        engine.animation_manager.draw(screen)
        engine.draw_overlays(screen)
        engine.transition_manager.draw(screen)
        engine._draw_notifications(screen)
        pygame.display.flip() # Display the updated screen
    # Finalize
    pygame.quit()

if __name__ == "__main__": # If this script is run directly the game will start
    main()