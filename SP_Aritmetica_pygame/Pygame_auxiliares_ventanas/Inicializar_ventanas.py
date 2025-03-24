import pygame
from Pygame_herramientas.Ventana import *
from Pygame_herramientas.Boton import *
from Pygame_herramientas.Inputs import *
from Pygame_herramientas.Creacion_botones import *

def inicializar_ventanas(ventana_principal, set_caption: str, path_sonido: str = None):
    """Esta funcion inicializa ventanas.

    Args:
        ventana_principal (_type_): Ventana principal del juego.
        set_caption (str): El set_caption de la ventana.
        path_sonido (str, optional): El path del sonido. Defaults to None.
    """
    reproducir_sonido_in(path_sonido)
    pygame.display.set_caption(set_caption)
    ventana_principal, fondo = inicializar_ventana()
    return ventana_principal, fondo

def inicializar_juego(ventana_principal, diccionario: dict) -> tuple:
    """Inicializa las variables del juego.

    Args:
        ventana_principal (_type_): La ventana donde sucede el juego.
        diccionario (_type_): _description_

    Returns:
        _type_: _description_
    """
    ventana_principal, fondo = inicializar_ventana()
    fuente = pygame.font.SysFont("arial", 30)
    fuente_2 = pygame.font.SysFont("arial", 20)
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    opciones_mostradas = False
    tiempo_extra = 0
    tiempo_transcurrido = 0
    input_respuesta = crear_input(ventana_principal, ("Arial", 20), "white", "gray", (200, 350), (200, 32), "white", "Respuesta")
    lista_boton = crear_botones_comodines(ventana_principal)
    return ventana_principal, fuente, fuente_2, clock, start_time, opciones_mostradas, tiempo_extra, tiempo_transcurrido, input_respuesta, lista_boton, fondo