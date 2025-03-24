import pygame

from Pygame_auxiliares_ventanas.Inicializar_ventanas import *
from Pygame_auxiliares_ventanas.Componentes import *
from Pygame_auxiliares_ventanas.Blit_ventanas import *
from Pygame_auxiliares_ventanas.Eventos import *

def rules(ventana_principal, diccionario_banderas):
    """Esta funcion es la encargada de ejecuttar la ventana.

    Args:
        ventana_principal (_type_): La ventana donde se muestran las reglas.
        diccionario_banderas (_type_): Diccionario que contiene informacion respecto a las ventanas.
    """
    reproducir_sonido_in("Sounds/click.mp3")
    reproducir_musica_fondo("Sounds/fondo.mp3")
    ventana_principal, fondo = inicializar_ventanas(ventana_principal, "Reglas", "Sounds/click.mp3")
    boton_volver, fuente_texto = crear_componentes_reglas(ventana_principal)

    lista_reglas = [
        "1-Comienzas con 3 vidas.",
        "2-La dificultad es progresiva, iniciando en facil hasta super dificil.",
        "3-Tienes 10 segundos para responder.",
        "4-Si respondes bien sumas 1 punto.",
        "5-Si la respuesta es incorrecta o se acaba el tiempo pierdes una vida.",
        "6-El juego termina cuando completas el nivel super dificil o pierdes todas tus vidas.",
        "7-Tenes 3 comodines para usar a tu favor, no los desperdicies..."
    ]
    
    while diccionario_banderas["bandera_rules"]:
        lista_eventos = pygame.event.get()

        diccionario_banderas = manejar_eventos_reglas(lista_eventos, diccionario_banderas, boton_volver)
        
        dibujar_reglas(ventana_principal, fondo, lista_reglas, boton_volver, fuente_texto)