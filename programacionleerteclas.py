import pygame
import sys
import eleccion_del_jugador

def leer_eventos():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:         #si le das a la equis que se salga
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:       #si le as dado a una tecla
            if evento.key == pygame.K_ESCAPE:  #si la tecla es esc que se salga
                print("Saliendo...")
                pygame.quit()
                sys.exit()
            resultado = eleccion_del_jugador.select_scenary(evento.key)         #devuelve que opcion esta seleccionada
            if resultado is not None:
                return resultado
    return None
