import random

def otorgar_opciones(problema_aleatorio: dict) -> list:
    """Esta funcion le otorga opciones de respuestas al jugador.

    Args:
        problema_aleatorio (int): El problema que tiene que resolver el jugador.
    """
    lista_opciones = []
    respuesta = problema_aleatorio["Respuestas"]
    numero_aleatorio = random.randint(1, 100)
    opcion_1 = respuesta - numero_aleatorio
    opcion_2 = respuesta + numero_aleatorio
    opcion_3 = respuesta + 5
    lista_opciones = [opcion_1, opcion_2, opcion_3, respuesta]

    return lista_opciones