import pygame

from Pygame_herramientas.Boton import *
from Pygame_herramientas.Inputs import *
from Pygame_herramientas.Ventana import *

def dibujar_bienvenida(ventana_principal, fondo, texto_renderizado, lista_botones, input_nombre):
    """Dibuja la ventana de bienvenida.

    Args:
        ventana_principal (_type_): La ventana donde se muestra la bienvenida.
        fondo (_type_): El fondo de la ventana.
        texto_renderizado (_type_): El texto.
        lista_botones (_type_):Los botones para volver atras o continuar.
        input_nombre (_type_): El espacio donde el jugador escribe el nombre.
    """
    ventana_principal.blit(fondo, (0, 0))
    if texto_renderizado:
        ventana_principal.blit(texto_renderizado, (150, 100))
    dibujar_botones(lista_botones)
    dibujar_input(input_nombre)
    pygame.display.update()

def dibujar_reglas(ventana_principal, fondo, lista_reglas, boton_volver, fuente_texto):
    """Dibuja las relas en la ventana.

    Args:
        ventana_principal (_type_): La ventana donde se muestran las reglas.
        fondo (_type_): El fondo donde se muestran las reglas.
        lista_reglas (list): Las reglas
        boton_volver (_type_): El boton para volver de la ventana.
        fuente_texto (_type_): La fuente del texto de las reglas.
    """
    ventana_principal.blit(fondo, (0, 0))
    dibujar_boton(boton_volver)
    
    y_offset = 50
    for regla in lista_reglas:
        texto_renderizado = fuente_texto.render(regla, True, "white")
        ventana_principal.blit(texto_renderizado, (0, y_offset))
        y_offset += 40

    pygame.display.update()

def mostrar_estado_juego(ventana_principal, diccionario: dict, fuente_2):
    """Muestra el estado del juego.

    Args:
        ventana_principal (_type_): La ventana donde se mostrara el estado del juego.
        diccionario (_type_): Diccionario con informacion a cerca del estado del juego.
        fuente_2 (_type_): La fuente con la que se mostrara el texto.
    """
    puntuacion_renderizadas = fuente_2.render(f"Puntos: {str(diccionario['Puntuacion'])}", True, "white")
    ventana_principal.blit(puntuacion_renderizadas, (50, 50))
    vidas_renderizadas = fuente_2.render(f"Vidas: {str(diccionario['Vidas'])}", True, "white")
    ventana_principal.blit(vidas_renderizadas, (50, 80))
    comodines_renderizados = fuente_2.render(f"Comodines: {str(diccionario['Comodines'])}", True, "white")
    ventana_principal.blit(comodines_renderizados, (50, 110))

def mostrar_problema(ventana_principal, problema: int, fuente, diccionario: dict):
    """Muestra el problema a resolver

    Args:
        ventana_principal (_type_): La ventana donde se mostrara el problema.
        problema (_type_): El problema a resolver.
        fuente (_type_): La fuente con la que se mostrara el texto.
        diccionario (_type_): Diccionario con informacion a cerca del estado del juego.
    """
    if diccionario["Rondas"] < 13 and diccionario["Vidas"] > 0:
        problema_renderizados = fuente.render(str(problema["Problema"]), True, "white")
        ventana_principal.blit(problema_renderizados, (250, 200))

def mostrar_iconos(ventana_principal):
    mostrar_icono(ventana_principal, "Iconos/tiempo.png", 25, 25, 20, 20)
    mostrar_icono(ventana_principal, "Iconos/score.png", 25, 25, 20, 50)
    mostrar_icono(ventana_principal, "Iconos/vidas.png", 25, 25, 20, 80)
    mostrar_icono(ventana_principal, "Iconos/comodines.png", 25, 25, 20, 110)

def mostrar_mensaje_final(ventana_principal, diccionario: dict, diccionario_banderas: dict, fondo, fuente):
    """Muestra un mensaje al jugador sobre si gano o perdio.

    Args:
        ventana_principal (_type_): La ventana donde se mostrara el mensaje.
        diccionario (_type_): Diccionario con informacion sobre el estado del jugador.
        diccionario_banderas (_type_): Diccionario con informacion sobre el estado de las ventanas del juego.
        fondo (_type_): El fondo de la ventana.
        fuente (_type_): La fuente del texto del mensaje.
    """
    if diccionario["Rondas"] == 12:
        ventana_principal.fill("white")
        mostrar_icono(ventana_principal, "Iconos/win.png", 200, 200, 200, 200)
        mostrar_icono(ventana_principal, "Iconos/trofeo.png", 100, 100, 250, 100)
        pygame.display.update()
        pygame.time.wait(2000)
        diccionario_banderas["bandera_play"] = False 
    
    elif diccionario["Vidas"] <= 0:
        ventana_principal.fill("white")
        mostrar_icono(ventana_principal, "Iconos/game_over.png", 600, 600, 0, 0)
        mostrar_icono(ventana_principal, "Iconos/perdiste.png", 100, 100, 250, 250)
        pygame.display.update()
        pygame.time.wait(2000)
        diccionario_banderas["bandera_play"] = False 

def mostrar_opciones(opciones_mostradas: bool, lista_opciones: list, ventana_principal, fuente):
    """Ejecuta la opcion de mostrar opciones.

    Args:
        opciones_mostradas (_type_): Dice si las opciones deben ser mostradas o no.
        lista_opciones (_type_): Las opciones a mostrar.
        ventana_principal (_type_): La ventana donde se mostraran las opciones.
        fuente (_type_): La fuente del texto.
    """
    if opciones_mostradas:
        opciones_texto = ",".join(map(str, lista_opciones))
        opciones_renderizadas = fuente.render(opciones_texto, True, "white")
        ventana_principal.blit(opciones_renderizadas, (200, 260))

def mostrar_estado(ventana_principal, fondo, diccionario, diccionario_banderas, fuente, fuente_2, problema, opciones_mostradas, lista_opciones):
    ventana_principal.blit(fondo,(0,0))
    mostrar_estado_juego(ventana_principal, diccionario, fuente_2)
    mostrar_problema(ventana_principal, problema, fuente, diccionario)
    mostrar_mensaje_final(ventana_principal, diccionario, diccionario_banderas, fondo, fuente)
    mostrar_opciones(opciones_mostradas, lista_opciones, ventana_principal, fuente)