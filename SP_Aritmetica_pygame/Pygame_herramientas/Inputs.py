import pygame

def crear_input(ventana, fuente, color_activo, color_inactivado, posicion, dimensiones, color_texto, placeholder = "") -> dict:
    """Esta funcion crea un input.

    Args:
        ventana (_type_): La surface del juego.
        fuente (_type_): La fuente del texto.
        color_activo (_type_): Color del input cuando esta activo.
        color_inactivado (_type_): Color de input cuando esta inactivo.
        posicion (_type_): La posicion en x, y.
        dimensiones (_type_): Las dimensiones del input.
        color_texto (_type_): Color del texto cuando escribe.
        placeholder (str, optional): El texto que contiene el placeholder.

    Returns:
        dict: El diccionario con todas las caracteristicas del input
    """
    input = {}
    input["Ventana"] = ventana
    input["Fuente"] = pygame.font.SysFont(fuente[0], fuente[1])
    input["Color_activo"] = color_activo
    input["Color_inactivo"] = color_inactivado
    input["Texto"] = ""
    input["Color_texto"] = color_texto
    input["Activo"] = False
    input["Rectangulo"] = pygame.Rect(posicion[0], posicion[1], dimensiones[0], dimensiones[1])
    input["Color_actual"] = color_inactivado
    input["Placeholder"] = placeholder
    input["Mostrar_placeholder"] = True

    return input

def dibujar_input (input: dict) -> None:
    """Esta funcion dibuja el input.

    Args:
        input (dict): El diccionario del input.
    """
    if input["Texto"] == "" and input["Mostrar_placeholder"]:
        superficie = input["Fuente"].render(str(input["Placeholder"]),False, "gray")
    else:
        superficie = input["Fuente"].render(str(input["Texto"]), False, input["Color_texto"])

    input["Ventana"].blit(superficie, (input["Rectangulo"].x + 5, input["Rectangulo"].y + 7))
    pygame.draw.rect(input["Ventana"], input["Color_actual"], input["Rectangulo"], 2)

def cambiar_color_input(input: dict):
    """Esta funcion cambia de color el input dependiendo si esta activo o inactivo.

    Args:
        input (dict): El diccionario del input. 
    """
    if input["Activo"]:
        input["Activo"] = False
        input["Color_actual"] = input["Color_inactivo"]
        if input["Texto"] == "":
            input["Mostrar_placeholder"] = True
    else:
        input["Activo"] = True
        input["Color_actual"] = input["Color_activo"]
        input["Mostrar_placeholder"] = False

def escribir_input (input: dict, evento) -> str:
    """Esta funcion nos ayuda a escribir en el input, hacer que
    podamos precionar enter, la barra espaciadora y que no se nos
    escape el texto del input.

    Args:
        input (dict): El diccionario del input. 
        evento (_type_): El evento del juego.

    Returns:
        str: Lo que se escribio en el input.
    """
    superficie = input["Fuente"].render(input["Texto"], True, input["Color_texto"])
    ancho_texto = superficie.get_width()
    nombre = ""

    if evento.key == pygame.K_RETURN:
        nombre = input["Texto"]
        input["Texto"] = ""
    elif evento.key == pygame.K_BACKSPACE:
        input["Texto"] = input["Texto"][:-1]
    else:
        if len(input["Texto"]) < (input["Rectangulo"].width - 20) // input["Fuente"].size(" ")[0]:
            input["Texto"] += evento.unicode

    return nombre