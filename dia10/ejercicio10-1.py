import pygame

"""Con pygame.init inicializamos pygame"""
pygame.init()
"""Pantalla de 800 pixeles por 600 pixeles"""
pantalla = pygame.display.set_mode((800, 600))

"""Bloque de código que da la lógica necesaria para mantener la pantalla activa y a la vez cerrarla cuando se desee
La pantalla estará ejecutándose siempre, pero si se detecta el evento QUIT (cuando se presiona la X para cerrar
la ventana, el argumento pasa a False y se termina el programa."""
se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False



