import pygame

def crear_boton (ventana, dimensiones, posicion, texto = None, fuente = None, path_imagen = None) -> dict:
    """Esta funcion crea un boton.

    Args:
        ventana (_type_): La surface del juego.
        dimensiones (_type_): Dimensiones del boton.
        posicion (_type_): Posicion en x, y.
        texto (_type_, optional): En caso de tener texto, el texto que contiene.
        fuente (_type_, optional): En caso de tener texto, la fuente del texto.
        path_imagen (_type_, optional): En caso de tener imagen, el path de la imagen.

    Returns:
        _type_: El diccionario del boton.
    """
    boton = {}
    boton["Ventana"] = ventana
    boton["Dimensiones"] = dimensiones
    boton["Posicion"] = posicion
    boton["Precionado"] = False
    
    if path_imagen != None:
        superficie_imagen = pygame.image.load(path_imagen)
        boton["Superficie"] = pygame.transform.scale(superficie_imagen, boton["Dimensiones"])
    else:
        fuente = pygame.font.SysFont(fuente[0], fuente[1])
        texto_fuente = fuente.render(texto, True, "black", "gray")
        boton["Superficie"] = texto_fuente

    boton["Rectangulo"] = boton["Superficie"].get_rect()
    boton["Rectangulo"].topleft = boton["Posicion"]

    return boton

def dibujar_boton(boton: dict):
    """Esta funcion dibuja un boton.

    Args:
        boton (_type_): El diccionario del boton.
    """
    boton["Ventana"].blit(boton["Superficie"], boton["Posicion"])

def dibujar_botones(lista: list):
    """Esta funcion recorre una lista de botones y los dibuja.

    Args:
        lista (_type_): La lista de botones.
    """
    for boton in lista:
        dibujar_boton(boton)

def reproducir_sonido_in (path_sonido: str):
    """Esta funcion reproduce un sonido para avanzar en el juego.

    Args:
        path_sonido (str): El path del sonido a reproducir.
    """
    pygame.mixer.init()
    pygame.mixer.music.load(path_sonido)
    pygame.mixer.music.play()

def reproducir_sonido_out (path_sonido: str):
    """Esta funcion reproduce un sonido para retroceder en el juego.

    Args:
        path_sonido (str): El path del sonido a reproducir.
    """
    pygame.mixer.init()
    pygame.mixer.music.load(path_sonido)
    pygame.mixer.music.play()

def reproducir_musica_fondo(path_musica: str):
    pygame.mixer.music.load(path_musica)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)