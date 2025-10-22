import pygame
import sys
import programacionleerteclas

vidapersonage=10

turno="jugador"

pygame.init()
pantalla = pygame.display.set_mode((400, 300))     #hay que borrarlo
pygame.display.set_caption("Menu principal")
monstruo="rata"
escenario = 0
def pelea(monstruo):
    while True:
        if monstruo=="rata":
            vidamonstruo=10
            dañofuerte=3
            dañodebil=1
        elif monstruo=="rana":
            vidamonstruo=11
            dañofuerte=3
            dañodebil=1
        elif monstruo=="señorcuchillo":
            vidamonstruo=12
            dañofuerte=1
            dañodebil=4
        if turno=="monstruo":
            if vidapersonage >=5:
                vidapersonage -= dañofuerte
                print(vidapersonage)
                turno="jugador"
            elif vidapersonage <=4:
                vidapersonage -= dañodebil
                print(vidapersonage)
                turno="jugador"
        if turno=="jugador":
            resultado = programacionleerteclas.leer_eventos()
            if ((resultado is not None) and (escenario == 0)) and ((not (vidapersonage<=0)) or (not (vidamonstruo<=0))):       #si resultado es algo y escenario es 0
                if resultado == "opcion1":                  #si el jugador selecciona opcion 1
                    print("Opción puñetazo seleccionada")
                    vidamonstruo -= 4
                    vidapersonage -=2
                    turno="monstruo"
                elif resultado == "opcion2":               #si el jugador selecciona opcion 2
                    print("Opción patada seleccionada")
                    vidamonstruo -= 2
                    turno="monstruo"
            elif vidapersonage <=0:
                print("Has perdido")
                pygame.quit()
                sys.exit()
            elif vidarata <=0:
                print("Has ganado")
                pygame.quit()
                sys.exit()
        pantalla.fill((30, 30, 30))
        pygame.display.flip()
