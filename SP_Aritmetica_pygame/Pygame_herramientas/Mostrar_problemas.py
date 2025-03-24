import pygame

def mostrar_texto(ventana_principal, fuente, texto, color, x, y):
    """Esta funcion muestra texto en pantalla.

    Args:
        ventana_principal (_type_): La surface del juego.
        fuente (_type_): La fuente del texto.
        texto (_type_): El texto a escribir.
        color (_type_): El color del texto.
        x (_type_): Coordenada en x.
        y (_type_): Coordenada en y.
    """
    superficie = fuente.render(texto, True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x, y)
    ventana_principal.blit(superficie, rectangulo)