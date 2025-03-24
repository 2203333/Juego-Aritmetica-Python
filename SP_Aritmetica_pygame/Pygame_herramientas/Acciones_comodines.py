from Package_dificultades_Y_Problemas.Espesificas import *
from .Boton import *
from Package_comodines.Comodines import *

def extender_tiempo(diccionario, tiempo_extra):
    reproducir_musica_fondo("Sounds/fondo.mp3")
    diccionario["Comodines"] -= 1
    tiempo_extra += 10

    return tiempo_extra


def dar_opciones(diccionario, problema, opciones_mostradas):
    reproducir_musica_fondo("Sounds/fondo.mp3")
    diccionario["Comodines"] -= 1
    lista_opciones = otorgar_opciones(problema)
    opciones_mostradas = True

    return lista_opciones, opciones_mostradas

def cambiar_problema(ventana_principal, diccionario, problemas_filtrados, fuente):
    reproducir_musica_fondo("Sounds/fondo.mp3")
    diccionario["Comodines"] -= 1
    problema = seleccionar_problema(diccionario, problemas_filtrados)
    problema_renderizados = fuente.render(str(problema["Problema"]), True, "white")
    ventana_principal.blit(problema_renderizados, (250,300))

    return problema