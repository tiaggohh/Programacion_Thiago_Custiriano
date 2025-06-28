import pygame


def crear_boton(dimensiones, posicion, ventana, color_borde, imagen = None,fuente = None ): #Constructor de un boton
    BOTON = {}
    BOTON["ventana"] = ventana
    BOTON["posicion"] = posicion
    BOTON["dimension"] = dimensiones
    BOTON["colorborde"] = color_borde
    BOTON["presionado"] = False
    
    if imagen != None:
        img = pygame.image.load(imagen)
        BOTON["superficie"] = pygame.transform.scale (img, BOTON["dimension"],)


    BOTON["rectangulo"] = BOTON["superficie"].get_rect()
    BOTON["rectangulo"].topleft = BOTON["posicion"]


    return BOTON

def dibujar_boton(BOTON: dict):
    BOTON["ventana"].blit(BOTON["superficie"], BOTON["posicion"])
    pygame.draw.rect(BOTON["ventana"], BOTON["colorborde"],BOTON ["rectangulo"], 10)
