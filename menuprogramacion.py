import pygame
import sys
import programacionleerteclas

pygame.init()
pantalla = pygame.display.set_mode((400, 300))     #hay que borrarlo
pygame.display.set_caption("Menu principal")

escenario = 0

while True:
    resultado = programacionleerteclas.leer_eventos()
    if resultado is not None and escenario == 0:       #si resultado es algo y escenario es 0
        if resultado == "opcion1":                  #si el jugador selecciona opcion 1
            print("Opción 1 seleccionada")
            escenario = 1
        elif resultado == "opcion2":               #si el jugador selecciona opcion 2
            print("Saliendo ...")
            pygame.quit()
            sys.exit()

    pantalla.fill((30, 30, 30))
    pygame.display.flip()
