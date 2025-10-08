class Engine:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} engine started.")


    def handle_event(self, event): # It means to handle events like keyboard input for the seleccion in the menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the event is to close the window
                running = False # It will stop the loop
            elif event.type == pygame.KEYDOWN:        # If a key is pressed
                if event.key == pygame.K_ESCAPE:      # If the key is Escape
                    pygame.quit() # It will close the window
                    sys.exit()  # And exit the program
                elif event.key == pygame.K_UP:          # If the key is the Up Arrow
                    print("Up") # It will print "Up"
                elif event.key == pygame.K_DOWN:        # If the key is the Up Arrow
                    print("Abajo") # It will print "Down"
                elif event.key == pygame.K_RETURN:    # If the key is Enter 
                    print("Enter") # It will print "Enter"
            
            self.Engine.handle_event(event)
    
    def update(self):
        self.all_sprites.update()

    def draw(self, screen):
        self.all_sprites.draw(screen)


    def stop(self):
        print(f"{self.name} engine stopped.")