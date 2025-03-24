def verificar_respuesta (problema: dict, respuesta: int) -> bool:
    """Verifica si la respuesta es correcta o no.

    Args:
        problema (dict): El problema a verificar.

    Returns:
        respuesta_final(bool): Si la respuesta es correcta o no.
    """
    respuesta_final = False
    respuesta = int(respuesta)

    if (respuesta == problema["Respuestas"]):
        respuesta_final = True

    return respuesta_final

def verificar_vidas (diccionario_juego: dict) -> bool:
    """Verifica la cantidad de vidas que le quedan al jugador.

    Args:
        diccionario_juego (dict): Diccionario que contiene informacion del estado del jugador.

    Returns:
        estado(bool): El estado del jugador.
    """
    estado = True

    if (diccionario_juego["Vidas"] == 0):
        estado = False
        
    return estado