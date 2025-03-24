import pygame

def inicializar_ventana() -> tuple:
   """Inicializa la ventana.

   Returns:
   ventana_principal, fondo(tuple): La ventana principal y el fondo.
   """
   ANCHO_VENTANA = 600
   ALTO_VENTANA = 600
   dimensiones_pantalla = (ANCHO_VENTANA, ALTO_VENTANA)

   pygame.init()
   pygame.mixer.init()
   
   ventana_principal =  pygame.display.set_mode(dimensiones_pantalla)
   icono = pygame.image.load(R"Iconos/math.jpg")
   pygame.display.set_icon(icono)
   
   fondo = pygame.image.load("Iconos/fondo_claro.jpg")
   fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))

   return ventana_principal, fondo

def mostrar_icono(ventana_principal, path_icono: str, ANCHO: int, ALTO: int, posicion_x: int, posicion_y: int) -> None:
   """Esta funcion muestra un icono.

   Args:
      ventana_principal (pygame.Surface): La superficie principal donde se muestra el icono.
      path_icono (str): El path del icono.
      ANCHO (int): El ancho del icono.
      ALTO (int): El alto del icono.
      posicion_x (int): La posición X del icono.
      posicion_y (int): La posición Y del icono.
   """
   icono = pygame.image.load(path_icono)
   icono = pygame.transform.scale(icono, (ANCHO, ALTO))
   ventana_principal.blit(icono, (posicion_x, posicion_y))

