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
posicion_cambio_horizontal = 0
posicion_cambio_vertical = 0


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Loop para que la pantala no desaparezca
se_ejecuta = True
while se_ejecuta:
    # RGB que da el color del fondo de pantalla
    pantalla.fill((201, 190, 175))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        "Función para mover el jugador horizontalmente"
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                posicion_cambio_horizontal = -0.05
            if evento.key == pygame.K_RIGHT:
                posicion_cambio_horizontal = 0.05
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                posicion_cambio_horizontal = 0
        "Función para mover el jugador verticalmente"
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                posicion_cambio_vertical = -0.05
            if evento.key == pygame.K_DOWN:
                posicion_cambio_vertical = 0.05
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                posicion_cambio_vertical = 0

    pos_x += posicion_cambio_horizontal
    pos_y += posicion_cambio_vertical
    jugador(pos_x, pos_y)
    pygame.display.update()
