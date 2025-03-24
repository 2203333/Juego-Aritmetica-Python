from Pygame_herramientas.Creacion_botones import *
from Pygame_herramientas.Inputs import *

def crear_componentes_bienvenida(ventana_principal):
    """Crea los componentes de la ventana

    Args:
        ventana_principal (_type_): La ventana donde se muestra la bienvenida.

    Returns:
        lista_botones
        boton_continuar
        boton_volver
        input_nombre
    """
    lista_botones = crear_botones_bienvenida(ventana_principal)
    boton_continuar = lista_botones[0]
    boton_volver = lista_botones[1]

    input_nombre = crear_input(
        ventana = ventana_principal,
        fuente = ("Arial", 20),
        color_activo = "white",
        color_inactivado = "gray",
        posicion = (200,200),
        dimensiones = (200,32),
        color_texto = "white",
        placeholder = "Nombre de usuario"
    )
    return lista_botones, boton_continuar, boton_volver, input_nombre

def crear_componentes_reglas(ventana_principal):
    """Crea los componentes de la ventana rules.

    Args:
        ventana_principal (_type_): La ventana donde se muestran las reglas.

    Returns:
        boton_volver
        fuente_texto
    
    """
    boton_volver = crear_boton_volver_rules(ventana_principal)
    fuente_texto = pygame.font.SysFont("consolas", 13)
    return boton_volver, fuente_texto

def crear_componentes_comodin(lista_boton: list) -> tuple:
    """Esta funcion asigna el boton del comodin a sus respectivas variables.

    Args:
        lista_boton (list): La lista de botones.

    Returns:
        tuple: Tupla de variables.
    """
    comodin_cambiar_problema = lista_boton[0]
    comodin_tiempo_extra = lista_boton[1]
    comodin_opciones = lista_boton[2]

    return comodin_cambiar_problema, comodin_tiempo_extra, comodin_opciones