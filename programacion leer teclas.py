import pygame
import sys
import eleccion_del_jugador

escenario = 0

pygame.init()

pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Lectura de teclas")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                print("Saliendo...")
                pygame.quit()
                sys.exit()
            resultado = eleccion_del_jugador.select_scenary(evento.key)
            if escenario == 0 and resultado is not None:
                if resultado == "opcion1":
                    print("Opción 1 seleccionada")
                    escenario = 1
                elif resultado == "opcion2":
                    print("saliendo ...")
                    pygame.quit()
                    sys.exit()
    pantalla.fill((30, 30, 30))
    pygame.display.flip()
