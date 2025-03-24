import pygame
from Pygame_herramientas.Boton import *

def salir (bandera):
    """Esta funcion cambia la bandera que se pasa como parametro para salir de una ventana.

    Args:
        bandera (_type_): La bandera.

    Returns:
        _type_: La bandera con el parametro cambiado.
    """
    reproducir_sonido_out("Sounds/click_reversed.mp3")
    pygame.time.wait(800)
    bandera = False

    return bandera