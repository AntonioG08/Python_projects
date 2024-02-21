import pygame
pygame.init()
pantalla = pygame.display.set_mode((800, 600))


# Titulo e icono
pygame.display.set_caption("Invasión espacial")
icono = pygame.image.load("espada-de-luz.png")
pygame.display.set_icon(icono)

# Jugador
img_jugador = pygame.image.load("astronave.png")
"Recordar que el icono es de 64px largo x ancho, muy importante al momento de ubicarlo espacialmente"
pos_x = 368
pos_y = 536


def jugador():
    pantalla.blit(img_jugador, (pos_x, pos_y))


# Loop para que la pantala no desaparezca
se_ejecuta = True
while se_ejecuta:
    "Pondremos el color de pantalla hasta el inicio para que no tape a nadie"
    pantalla.fill((201, 190, 175))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
    jugador()
    pygame.display.update()
