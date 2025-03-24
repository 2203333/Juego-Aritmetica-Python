import pygame

from Package_auxiliares.Auxiliares import *
from Pygame_auxiliares_ventanas.Inicializar_ventanas import *
from Pygame_auxiliares_ventanas.Componentes import *
from Pygame_auxiliares_ventanas.Blit_ventanas import *
from Pygame_auxiliares_ventanas.Eventos import *

estados_del_juego = {}
estados_del_juego["Vidas"] = True

def jugar(ventana_principal, diccionario_banderas: dict, diccionario: dict):
    """Ejecuta la ventana donde el usuario podra jugar.

    Args:
        ventana_principal (_type_): La ventana donde se llevara a cabo el juego.
        diccionario_banderas (_type_): Diccionario con informacion sobre el estado de las ventanas del juego.
        diccionario (_type_): Diccionario con informacion a cerca del estado del jugador.
    """
    reproducir_musica_fondo("Sounds/fondo.mp3")
    tiempo_limite = 15
    lista_opciones = []
    problema = seleccionar_problema(diccionario, problemas_filtrados)
    ventana_principal, fuente, fuente_2, clock, start_time, opciones_mostradas, tiempo_extra, tiempo_transcurrido, input_respuesta, lista_boton, fondo = inicializar_juego(ventana_principal, diccionario)
    comodin_cambiar_problema, comodin_tiempo_extra, comodin_opciones = crear_componentes_comodin(lista_boton)

    while diccionario_banderas["bandera_play"]:
        lista_eventos = pygame.event.get()
        mostrar_estado(ventana_principal, fondo, diccionario, diccionario_banderas, 
                        fuente, fuente_2, problema, opciones_mostradas, lista_opciones)

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                manejar_clic_input(input_respuesta, evento)
                problema, tiempo_extra, lista_opciones, opciones_mostradas = manejar_comodines(evento, diccionario, comodin_cambiar_problema, 
                                                                                                    comodin_tiempo_extra, comodin_opciones, ventana_principal, 
                                                                                                    problemas_filtrados, fuente, problema, tiempo_extra, 
                                                                                                    lista_opciones, opciones_mostradas)
            elif evento.type == pygame.KEYDOWN:
                respuesta = guardar_respuesta_input(input_respuesta, evento)
                if evento.key == pygame.K_RETURN:
                    opciones_mostradas, start_time, problema, tiempo_extra = manejar_evento_respuesta(problema, diccionario, respuesta, 
                                                                                                    tiempo_transcurrido, tiempo_limite, tiempo_extra)
            if evento.type == pygame.QUIT:
                manejar_evento_cierre(diccionario_banderas)

        dibujar_input(input_respuesta)
        dibujar_botones(lista_boton)
        mostrar_iconos(ventana_principal)
        tiempo_transcurrido = (pygame.time.get_ticks() - start_time) // 1000
        cronometro = fuente_2.render(f"Tiempo: {tiempo_transcurrido}", False, "white")
        ventana_principal.blit(cronometro, (50,20))
        clock.tick(60)
        pygame.display.update()

    guardar_puntuacion("Puntuacion.json", diccionario)