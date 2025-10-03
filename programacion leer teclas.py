import pygame
import sys

# Inicializar Pygame
pygame.init()

# Crear una ventana (requerido para recibir eventos)
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Lectura de teclas")

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:          # Si evento es = a Cerrar pygame
            pygame.quit()                        # Cerrar Pygame
            sys.exit()
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
    # Opcional: color de fondo
    pantalla.fill((30, 30, 30))
    pygame.display.flip()
