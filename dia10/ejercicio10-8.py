import random
import pygame

pygame.init()
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Invasión espacial")
icono = pygame.image.load("espada-de-luz.png")
pygame.display.set_icon(icono)
"Código para cargar y desplegar el fondo de la pantalla de juego"
fondo = pygame.image.load("Space_Background.png")

# Variables del Jugador
"64 Px mide la imagen de la nave"
img_jugador = pygame.image.load("astronave.png")
"Variables de posición inicial"
pos_x = 368
pos_y = 536
"Variables para modificar la posición inicial"
posicion_cambio_horizontal = 0
posicion_cambio_vertical = 0

# Variables del Enemigo
img_enemigo = pygame.image.load("enemigo.png")
"Variables de posición inicial"
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(0, 200)
"Variables para modificar la posición inicial"
enemigo_cambio_horizontal = 3
enemigo_cambio_vertical = 35

# Variables de la munición
img_bala = pygame.image.load("Ammo.png")
"Variables de posición inicial"
bala_x = 0
bala_y = 0
"Variables para modificar la posición inicial"
bala_cambio_x = 0
bala_cambio_y = 3
"Variables para visualizar la bala hasta que sea disparada"
bala_visible = False


# Función Jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Función Enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))


# Función disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    "Agregamos la suma de pixeles, por que queremos que el misil surga de la mitad de la nave"
    pantalla.blit(img_bala, (x + 19, y + 10))


# Loop para que la pantala no desaparezca
se_ejecuta = True
while se_ejecuta:
    pantalla.blit(fondo, (0, 0))

    # Loop que detecta eventos que ocurren en el juego
    for evento in pygame.event.get():
        "Función para cerrar el juego al presionar EXIT"
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        "Función para mover el jugador horizontalmente"
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                posicion_cambio_horizontal = -2
            if evento.key == pygame.K_RIGHT:
                posicion_cambio_horizontal = 2
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                posicion_cambio_horizontal = 0

        "Función para mover el jugador verticalmente"
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                posicion_cambio_vertical = -2
            if evento.key == pygame.K_DOWN:
                posicion_cambio_vertical = 2
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                posicion_cambio_vertical = 0

        "Función para disparar la bala"
        if not bala_visible:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    disparar_bala(pos_x, pos_y)
                    bala_x = pos_x
                    bala_y = pos_y

    # Actualizar las posiciones X y Y del JUGADOR
    pos_x += posicion_cambio_horizontal
    pos_y += posicion_cambio_vertical

    # Condicional para mantener en los bordes al JUGADOR
    if pos_x <= 0:
        pos_x = 0
    elif pos_x >= 736:
        pos_x = 736
    elif pos_y <= 0:
        pos_y = 0
    elif pos_y >= 536:
        pos_y = 536

    # Actualizar las posiciones X y Y del ENEMIGO
    enemigo_x += enemigo_cambio_horizontal

    # Condicional para mantener en los bordes al ENEMIGO
    if enemigo_x <= 0:
        enemigo_cambio_horizontal = 2
        enemigo_y += enemigo_cambio_vertical
    elif enemigo_x >= 736:
        enemigo_cambio_horizontal = -2
        
        enemigo_y += enemigo_cambio_vertical

    # Actualizar el movimiento de la bala
    if bala_y <= -32:
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_cambio_y

    # Llamada del jugador y el enemigo
    jugador(pos_x, pos_y)
    enemigo(enemigo_x, enemigo_y)

    # Actualizar lo que estamos viendo en pantalla
    pygame.display.update()
