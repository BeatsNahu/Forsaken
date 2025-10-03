import pygame
import sys

escenario=0
salir="no seleccionado"
jugar="seleccionado"
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
                if escenario==0:
                    jugar="seleccionado"
                    if salir=="seleccionado":
                        salir="no seleccionado"
            elif evento.key == pygame.K_DOWN:            # Si Tecla = Flecha Abajo
                if escenario==0:
                    salir="seleccionado"
                    if jugar=="seleccionado":
                        jugar="no seleccionado"
            elif evento.key == pygame.K_RETURN:                  # Si Tecla = a Enter 
                if escenario==0:
                    if jugar=="seleccionado":
                        escenario=1
                        print(escenario)
                    elif salir=="seleccionado":
                        print("Saliendo...")
                        pygame.quit()
                        sys.exit()
    # Opcional: color de fondo
    pantalla.fill((30, 30, 30))
    pygame.display.flip()
