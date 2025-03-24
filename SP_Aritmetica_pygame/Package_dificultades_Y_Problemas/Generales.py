import random

def seleccionar_dificultad (contador_vueltas: int) -> str:
    """Selecciona la dificulad del juego dependendiento de la cantidad de rondas.

    Args:
        contador_vueltas (int): La cantidad de rondas jugadas por el jugador.

    Returns:
        dificulatd(str): La dificultad
    """
    dificultad = "Baja"

    if (contador_vueltas >= 3 and contador_vueltas <= 7):
        dificultad = "Media"
    elif (contador_vueltas > 7 and contador_vueltas <= 10):
        dificultad = "Alta"
    elif (contador_vueltas > 10):
        dificultad = "Super alta"

    return dificultad

def filtrar_problemas_por_dificultad(datos_normalizados: list) -> dict:
    """Filtra los problemas por su dificultad una sola vez al inicio y los almacena en un diccionario.
    
    Args:
        datos_normalizados (list): La lista de diccionarios con los datos.
    
    Returns:
        dict: Un diccionario con listas de problemas filtrados por cada dificultad.
    """
    problemas_filtrados = {
        "Baja": [],
        "Media": [],
        "Alta": [],
        "Super alta": []
    }
    
    for problema in datos_normalizados:
        dificultad = problema["Dificultad"]

        try:
            problemas_filtrados[dificultad].append({
                "Problema": problema["Problema"],
                "Respuestas": int(problema["Respuestas"])
            })
        except KeyError:
            pass

    return problemas_filtrados

def obtener_problema_aleatorio (lista_problemas: dict) -> str:
    """Obtiene un problema aleaorio de una lista de problemas.

    Args:
        lista_problemas (list): La lista donde se encuetran los problemas.

    Returns:
        problema(str): El problema seleccionado aleatoriamente.
    """
    problema = random.choice(lista_problemas)
    lista_problemas.remove(problema)
    
    return problema