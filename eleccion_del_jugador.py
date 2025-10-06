import pygame
opcion1 = "seleccionado"
opcion2 = "no seleccionado"

def select_scenary(key):
    global opcion1, opcion2
    if key == pygame.K_UP:                  # Si Tecla = a flecha arriba 
        opcion1 = "seleccionado"
        opcion2 = "no seleccionado"
    elif key == pygame.K_DOWN:                  # Si Tecla = a flecha abajo 
        opcion2 = "seleccionado"
        opcion1 = "no seleccionado"
    elif key == pygame.K_RETURN:                  # Si Tecla = a Enter 
        if opcion1=="seleccionado":
            return ("opcion1")
        elif opcion2=="seleccionado":
            return ("opcion2")
    return None