import re, datetime, json

def parser_csv (path:str) -> list:
    """Parsea un archivo csv.

    Args:
        path (str): El path del archivo csv.

    Returns:
        lista_calculos(list): La lista de diccionarios con los datos.
    """
    lista_calculos = []
    
    with open(path, "r" , encoding="utf8") as archivo:
        archivo.readline()
        for linea in archivo:
            diccionario = {}
            valores = re.split(',|\n',linea)
            diccionario["Dificultad"] = valores[0]
            diccionario["Problema"] = valores[1]
            diccionario["Respuestas"] = valores[2]

            lista_calculos.append(diccionario)

    return lista_calculos

def guardar_puntuacion(path: str, diccionario: dict) -> None:
    """Guarda la puntuacion del jugador en un archivo json

    Args:
        path (str): El path del archivo.
        diccionario (dict): El diccionario donde se encuentra la punuacion.
    """
    fecha = datetime.date.today().isoformat()
    try:
        with open(path, "r", encoding="utf8") as archivo:
            lista_puntuacion = json.load(archivo)
    except FileNotFoundError:
        lista_puntuacion = []

    lista_puntuacion.append({
        "Nombre": diccionario["Nombre"],
        "Puntuacion": diccionario["Puntuacion"],
        "Fecha": fecha
    })
    with open(path, "w", encoding="utf8") as archivo:
        json.dump(lista_puntuacion, archivo, indent=4)