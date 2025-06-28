import pygame
from Boton import *
import random


ANCHO_VENTANA = 800

LARGO_VENTANA = 500

pygame.init()   

VENTANA = pygame.display.set_mode ((ANCHO_VENTANA, LARGO_VENTANA))
pygame.display.set_caption("Mi primer videojuego (Proyecto GTA 6")
icono = pygame.image.load("utn_icono.jpg")
pygame.display.set_icon(icono)
#gatito = pygame.image.load("gatito.jpeg")

Boton_gatito = crear_boton(dimensiones = (100,100),
                           posicion = (50,50),
                           ventana = VENTANA,
                           imagen ="gatito.jpeg",
                           color_borde = "Green")

Fuente_texto = pygame.font.SysFont("Arial",20)

flag_run = True #para q se abra y on se cierre
while flag_run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #para q se pueda cerrar
            flag_run = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if Boton_gatito ["rectangulo"].pygame.Rect.collidepoint(evento.pos):
                texto = Fuente_texto.render("Miaw", False, "Blue", "Pink")
                x = random.randint(50,700)
                y = random.randint(50,500)

                VENTANA.blit (texto, (x,y))

    
    dibujar_boton(Boton_gatito)


    #VENTANA.fill ("green")
    #VENTANA.blit (icono,(500,50))
    #VENTANA.blit (gatito,(100,25))


    pygame.display.update()

pygame.quit()