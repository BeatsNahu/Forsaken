def Menu():
    menu = pygame.image.load("assets/backgrounds/prueba_menu.jpg").convert()
    menu = pygame.transform.scale(menu, (1080, 720))

    while True:

        screen.blit(menu,(0, 0))

        if evento.type == pygame.KEYDOWN:        # Si se presiona una tecla
            if evento.key == pygame.K_ESCAPE:      # Si Tecla = Esc
                print("Saliendo...")
                pygame.quit()
                sys.exit()
            elif evento.key == pygame.K_UP:          # Si Tecla = Flecha Arriba
                print("Arriba")
            elif evento.key == pygame.K_DOWN:            # Si Tecla = Flecha Abajo
                print("Abajo")
            elif evento.key == pygame.K_KP_ENTER:                  # Si Tecla = a Enter 
                print("Enter")

        pygame.display.update()
        clock.tick(60)




