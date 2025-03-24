from .Boton import crear_boton

def crear_botones_comodines(ventana_principal) -> list:
    """Crea todos los botones de los comodines.

    Args:
        ventana_principal (_type_): La ventana donde se mostraran los botones.

    Returns:
        lista_botones_comodines(list): La lista con los botones creados.
    """
    comodin_cambiar_problema = crear_boton(ventana = ventana_principal,
                                        posicion = (195,440),
                                        dimensiones = (50,50),
                                        path_imagen = "Iconos/cambiar_pregunta.png")
    
    comodin_tiempo_extra = crear_boton(ventana = ventana_principal,
                                        posicion = (275,440),
                                        dimensiones = (50,50),
                                        path_imagen = "Iconos/tiempo_extra.png")
    
    comodin_opciones = crear_boton(ventana = ventana_principal,
                                        posicion = (355,440),
                                        dimensiones = (50,50),
                                        path_imagen = "Iconos/dar_opciones.png")
    
    lista_botones_comodines = [comodin_cambiar_problema, comodin_tiempo_extra, comodin_opciones]

    return lista_botones_comodines

def crear_boton_volver_rules(ventana_principal):
    """Crea el boton para volver de la ventana reglas.

    Args:
        ventana_principal (type): La ventana donde aparecera el boton.

    Returns:
        boton_volver
    """
    boton_volver = crear_boton(ventana = ventana_principal,
                        posicion = (280,340),
                        dimensiones = (40,40),
                        path_imagen = "Iconos/back.png")
    
    return boton_volver

def crear_botones_bienvenida(ventana_principal) -> list:
    """Crea todos los botones de la ventana bienvenida.

    Args:
        ventana_principal (_type_): La ventana donde se mostraran los botones.

    Returns:
        lista_botones_comodines(list): La lista con los botones creados.
    """
    boton_volver = crear_boton(ventana = ventana_principal,
                        posicion = (230,300),
                        dimensiones = (40,40),
                        path_imagen = "Iconos/back.png")
    boton_continuar = crear_boton(ventana = ventana_principal,
                        posicion = (330,300),
                        dimensiones = (40,40),
                        path_imagen = "Iconos/start.png")
    
    lista_botones_bienvenida = [boton_continuar, boton_volver]

    return lista_botones_bienvenida

def crear_botones_main(ventana_principal) -> list:
    """Crea todos los botones relacionados con el main.

    Args:
        ventana_principal (list): La ventana donde se mostraran los botones.

    Returns:
        lista_botones_comodines(list): La lista con los botones creados.
    """
    boton_play = crear_boton(ventana = ventana_principal,
                                posicion = (250,150),
                                dimensiones = (100,100),
                                path_imagen = "Iconos/boton-de-inicio.png")

    boton_rules = crear_boton(ventana = ventana_principal,
                                posicion = (275,100), 
                                dimensiones = (50,50),
                                path_imagen = "Iconos/reglas.png")

    boton_quit = crear_boton(ventana = ventana_principal,
                                posicion = (250,250),
                                dimensiones = (100,100),
                                path_imagen = "Iconos/puerta-de-salida.png")

    lista_boton = [boton_play, boton_rules, boton_quit]

    return lista_boton
