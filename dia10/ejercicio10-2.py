import pygame
pygame.init()

# Crea la pantalla 800p x 600p
pantalla = pygame.display.set_mode((800, 600))


# Titulo e icono
pygame.display.set_caption("Invasión espacial")
icono = pygame.image.load("espada-de-luz.png")
pygame.display.set_icon(icono)
"""Otra solución podría ser directo pygame.display.set_icon(pygame.image.load('espada-de-luz.png') aun que con esta 
forma se vuelve algo largo y podría ser confuso"""


# Loop para que la pantala no desaparezca
se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    "Todo lo que queramos que ocurra dentro de la pantalla debe ir dentro del loop"
    "Revisar colorspire.com para ver que código de tonalidad RGB nos gusta para el fondo"
    pantalla.fill((201, 190, 175))
    "Ya rellenamos del color que queriamos, pero falta actualizar esto para ver el cambio efectuado en la pantalla"
    pygame.display.update()

