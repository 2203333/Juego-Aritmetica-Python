from Package_dificultades_Y_Problemas.Generales import *

def seleccionar_problema (diccionario: dict, problemas_filtrados: dict) -> str:
    """Selecciona un problema llamando a otras funciones.

    Args:
        diccionario_juego (dict): El diccionario donde se encuentran daos del estado del juego.
        problemas_filtrados (list): Los datos filtrados.

    Returns:
        problema(str): El problema seleccionado.
    """
    dificultad = seleccionar_dificultad(diccionario["Rondas"])
    lista_problemas = problemas_filtrados[dificultad]
    problema = obtener_problema_aleatorio(lista_problemas)
    
    return problema