def crear_diccionario_juego (vidas: int, rondas: int, puntuacion: int, nombre_usuario: str, comodines: int) -> dict:
    """Esta funcion crea el diccionario del juego.

    Args:
        vidas (int): Cantidad de vidas
        rondas (int): Cantidad de rondas
        puntuacion (int): Cantidad de puntos

    Returns:
        dict: Diccionario del juego
    """
    diccionario = {"Nombre": nombre_usuario,
                    "Rondas": rondas,
                    "Puntuacion": puntuacion,
                    "Vidas": vidas,
                    "Comodines": comodines}
    
    return diccionario