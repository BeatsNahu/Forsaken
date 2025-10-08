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
        for event in pygame.event.get(): # Event handling loop
            Engine.handle_event(event) # Handle other events like keyboard
            
        # Update game state
        Engine.update() 

        # Screen rendering
        screen.fill((0, 0, 0))
        Engine.draw(screen)
>>>>>>> 9dd9a3f (Editing the main - engine - escene_maganer files and configuring them and eliminating extra files. I'm trying to do the first escene)
        pygame.display.flip() # Display the updated screen
=======
        pygame.display.flip()
>>>>>>> 4520943 (I created the initial game configuration)
=======
        pygame.display.flip() # Display the updated screen
>>>>>>> b6088aa (Merge)

        # Control frame rate
        clock.tick(60)

    # Finalize
    pygame.quit()

if __name__ == "__main__":
    main()