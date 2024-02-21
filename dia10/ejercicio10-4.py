import pygame
pygame.init()
pantalla = pygame.display.set_mode((800, 600))


# Titulo e icono
pygame.display.set_caption("Invasión espacial")
icono = pygame.image.load("espada-de-luz.png")
pygame.display.set_icon(icono)

# Jugador
"64 Px mide la imagen de la nave"
img_jugador = pygame.image.load("astronave.png")
pos_x = 368
pos_y = 536


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Loop para que la pantala no desaparezca
se_ejecuta = True
while se_ejecuta:
    # RGB que da el color del fondo de pantalla
    pantalla.fill((201, 190, 175))
    """"Usando estos comandos se puede modificar la posición inicial de nuestro icono, aun que por el momento no podemos
    Controlarlo nosotros, pasar a la siguiente lección para aprender de esto"""
    pos_x += 0.05
    pos_y -= 0.05
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    jugador(pos_x, pos_y)
    pygame.display.update()
