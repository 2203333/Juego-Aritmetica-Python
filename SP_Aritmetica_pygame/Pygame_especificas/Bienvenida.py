import pygame

from Pygame_especificas.Play import *
from Pygame_auxiliares_ventanas.Blit_ventanas import *

diccionario = crear_diccionario_juego(3, 0, 0, None, 3)

def dar_bienvenida(ventana_principal, diccionario_banderas):
    """Ejecuta la ventana de bienvenida.

    Args:
        ventana_principal (_type_): La ventana donde se muestra la bienvenida.
        diccionario_banderas (_type_): Diccionario con informacion sobre las ventanas del juego.
    """
    reproducir_sonido_in("Sounds/click.mp3")
    ventana_principal, fondo = inicializar_ventanas(ventana_principal, "Bienvenida", "Sounds/click.mp3")
    lista_botones, boton_continuar, boton_volver, input_nombre = crear_componentes_bienvenida(ventana_principal)
    
    evento_saludar = pygame.USEREVENT
    fuente = pygame.font.SysFont("arial", 30)
    texto_renderizado = None
    reproducir_musica_fondo("Sounds/fondo.mp3")

    while diccionario_banderas["bandera_bienvenida"]:
        lista_eventos = pygame.event.get()

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver["Rectangulo"].collidepoint(evento.pos):
                    reproducir_sonido_out("Sounds/click_reversed.mp3")
                    diccionario_banderas["bandera_bienvenida"] = False
                elif input_nombre["Rectangulo"].collidepoint(evento.pos):
                    cambiar_color_input(input_nombre)
                elif boton_continuar["Rectangulo"].collidepoint(evento.pos):
                    reproducir_sonido_in("Sounds/click.mp3")
                    diccionario_banderas["bandera_bienvenida"] = False
                    jugar(ventana_principal, diccionario_banderas, diccionario)
            elif evento.type == pygame.KEYDOWN:
                if input_nombre["Activo"]:
                    nombre = escribir_input(input_nombre, evento)
                    if evento.key == pygame.K_RETURN:
                        texto_renderizado = fuente.render(f"Bienvenido/a {nombre}", True, "white")
                        pygame.event.post(pygame.event.Event(evento_saludar))
                        diccionario["Nombre"] = nombre
            elif evento.type == pygame.QUIT:
                diccionario_banderas["bandera_bienvenida"] = False
                diccionario_banderas["bandera_run"] = False

        dibujar_bienvenida(ventana_principal, fondo, texto_renderizado, lista_botones, input_nombre)

        pygame.display.update()