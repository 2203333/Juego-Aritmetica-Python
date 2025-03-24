from os import system
system ("cls")

import pygame

from Pygame_especificas.Funciones_main import *
from Pygame_especificas.Rules import *
from Pygame_especificas.Bienvenida import *

def iniciar_juego():
    """Esta funcion es la encargada de iniciar el juego.
    """
    pygame.init()
    clock = pygame.time.Clock()
    reproducir_musica_fondo("Sounds/fondo.mp3")
    ventana_principal, fondo = inicializar_ventana()
    lista_botones = crear_botones_main(ventana_principal)
    boton_play = lista_botones[0]
    boton_rules = lista_botones[1]
    boton_quit = lista_botones[2]
    lista_botones_main = [boton_play, boton_rules, boton_quit]
    
    diccionario_banderas = {
        "bandera_run": True,
        "bandera_rules": True,
        "bandera_bienvenida": True,
        "bandera_play": True
    }

    while diccionario_banderas["bandera_run"]:
        pygame.display.set_caption("Aritmetica")
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_play["Rectangulo"].collidepoint(evento.pos):
                    diccionario_banderas["bandera_bienvenida"] = True
                    dar_bienvenida(ventana_principal, diccionario_banderas)
                    reproducir_musica_fondo("Sounds/fondo.mp3")
                elif boton_rules["Rectangulo"].collidepoint(evento.pos):
                    diccionario_banderas["bandera_rules"] = True
                    rules(ventana_principal, diccionario_banderas)
                    reproducir_musica_fondo("Sounds/fondo.mp3")
                elif boton_quit["Rectangulo"].collidepoint(evento.pos):
                    diccionario_banderas["bandera_run"] = salir(diccionario_banderas["bandera_run"])
            elif evento.type == pygame.QUIT:
                diccionario_banderas["bandera_run"] = False
        

        ventana_principal.blit(fondo,(0,0))
        dibujar_botones(lista_botones_main)

        clock.tick(60)
        pygame.display.update()

    pygame.mixer.music.stop()
    pygame.quit()

iniciar_juego()