import pygame

from Pygame_herramientas.Boton import *
from Pygame_herramientas.Acciones_comodines import *
from Pygame_herramientas.Inputs import *
from Package_verificaciones.Verificaciones import *
from Package_archivos.Archivos import *

datos_normalizados = parser_csv("Problemas.csv")
problemas_filtrados = filtrar_problemas_por_dificultad(datos_normalizados)

def manejar_eventos_reglas(lista_eventos, diccionario_banderas, boton_volver):
    """Maneja los eventos de la ventana.

    Args:
        lista_eventos (_type_): Los eventos de la ventana
        diccionario_banderas (_type_): Diccionario que contiene informacion respecto a las ventanas.
        boton_volver (_type_):El boton para volver a la ventana principal.

    Returns:
        diccionario_banderas (_type_): Diccionario que contiene informacion respecto a las ventanas.
    """
    for evento in lista_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["Rectangulo"].collidepoint(evento.pos):
                reproducir_sonido_out("Sounds/click_reversed.mp3")
                diccionario_banderas["bandera_rules"] = False
        elif evento.type == pygame.QUIT:
            diccionario_banderas["bandera_rules"] = False
            diccionario_banderas["bandera_run"] = False
    return diccionario_banderas

def manejar_comodines(evento, diccionario, comodin_cambiar_problema, comodin_tiempo_extra, comodin_opciones, ventana_principal, problemas_filtrados, fuente, problema, tiempo_extra, lista_opciones, opciones_mostradas):
    """Maneja el clic en los comodines disponibles."""
    if diccionario["Comodines"] > 0:
        if comodin_cambiar_problema["Rectangulo"].collidepoint(evento.pos):
            problema = cambiar_problema(ventana_principal, diccionario, problemas_filtrados, fuente)
        elif comodin_tiempo_extra["Rectangulo"].collidepoint(evento.pos):
            tiempo_extra = extender_tiempo(diccionario, tiempo_extra)
        elif comodin_opciones["Rectangulo"].collidepoint(evento.pos):
            lista_opciones, opciones_mostradas = dar_opciones(diccionario, problema, opciones_mostradas)
    return problema, tiempo_extra, lista_opciones, opciones_mostradas

def manejar_evento_cierre(diccionario_banderas):
    """Maneja el evento de cierre del juego."""
    diccionario_banderas["bandera_play"] = False
    diccionario_banderas["bandera_run"] = False

def manejar_clic_input(input_respuesta, evento):
    """Maneja el clic en el input de respuesta para cambiar su color."""
    if input_respuesta["Rectangulo"].collidepoint(evento.pos):
        cambiar_color_input(input_respuesta)

def guardar_respuesta_input(input_respuesta, evento):
    if input_respuesta["Activo"]:
        respuesta = escribir_input(input_respuesta, evento)
    return respuesta

def manejar_evento_respuesta(problema, diccionario, respuesta, tiempo_transcurrido, tiempo_limite, tiempo_extra):
    opciones_mostradas = False
    if verificar_respuesta(problema, respuesta) == True and tiempo_transcurrido < (tiempo_limite + tiempo_extra):
        diccionario["Puntuacion"] += 1
    else:
        diccionario["Vidas"] -= 1
    problema = seleccionar_problema(diccionario, problemas_filtrados)
    diccionario["Rondas"] += 1
    start_time =  pygame.time.get_ticks()
    tiempo_extra = 0

    return opciones_mostradas, start_time, problema, tiempo_extra