import math
import random
import pygame
from pygame import mixer

pygame.init()
pantalla = pygame.display.set_mode((800, 600))


# Sección de código donde van todas las VARIABLES divididas por CATEGORÍA
# Titulo e icono
pygame.display.set_caption("Invasión espacial")
icono = pygame.image.load("espada-de-luz.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Space_Background.png")

# Agregar música
mixer.music.load('Gasolina.mp3')
"El volúmen de la música va de 0 a 1"
mixer.music.set_volume(0.2)
mixer.music.play(-1)


# Variable del Jugador
"64 Px mide la imagen de la nave"
img_jugador = pygame.image.load("astronave.png")


# Variables del Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_cambio_horizontal = []
enemigo_cambio_vertical = []
cantidad_enemigos = 100

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(0, 100))
    enemigo_cambio_horizontal.append(3)
    enemigo_cambio_vertical.append(35)

# Variables de la munición
img_bala = pygame.image.load("Ammo.png")
"Variables para modificar la posición inicial"
bala_cambio_x = 0
bala_cambio_y = 3
"Variables para visualizar la bala hasta que sea disparada"
bala_visible = False

# Variable que almacena la puntuación actual
puntuaje = 0
"Variable del estilo de letra para visualizar el puntuaje"
"""La liberia pygame incluye SOLO esta fuente por default, si queremos usar otra necesitariamos bajarla y guardarla en 
la carpeta de python día 10 donde esta todo lo relacionado al juego, podríamos ir al sitio '1001freefonts' """
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10

# Texto final del juego
fuente_final = pygame.font.Font("freesansbold.ttf", 40)


# Bloque del código donde están todas las funciones que necesitaremos
# Función Jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Función Enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# Función disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    "Agregamos la suma de pixeles, por que queremos que el misil surga de la mitad de la nave"
    pantalla.blit(img_bala, (x + 19, y + 10))


# Función para detectar colisiones
def colision(x_1, y_1, x_2, y_2):
    """Usaremos la funcion de distancia conocida como ( (x2 - x1)^2 + (y2 - y1)^2)^1/2 """
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 25:
        return True
    else:
        return False


# Función mostrar puntuaje
def mostrar_puntuacion(x, y):
    """Antes de poder usar 'blit' como siempre, necesitamos primero crear el texto usando la siguiente linea"""
    texto = fuente.render(f"Puntuaje: {puntuaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Función para mostrar fin del juego
def texto_final():
    mi_fuente_final = fuente_final.render("PERDISTE, MARICA", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (200, 280))


def jugarsp(y):
    # Loop para que la pantala no desaparezca
    se_ejecuta = False
    x = 1
    if x == y:
        se_ejecuta = True

    "Variables para modificar la posición inicial"
    posicion_cambio_horizontal = 0
    posicion_cambio_vertical = 0

    "Variables de posición inicial del jugador principal"
    pos_x = 368
    pos_y = 536

    "Variables de posición inicial de la bala"
    bala_x = 0
    bala_y = 0

    "Variable que almacena la puntuación actual"
    global puntuaje, bala_visible

    sonido_misil = mixer.Sound('misil.mp3')
    sonido_misil.set_volume(0.2)
    sonido_colision = mixer.Sound("Boom.mp3")
    sonido_colision.set_volume(0.7)

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
                        sonido_misil.play()

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
        for i in range(cantidad_enemigos):
            # Fin del juego
            if enemigo_y[i] > 400:
                for k in range(cantidad_enemigos):
                    enemigo_y[k] = 1000
                texto_final()
                break
            enemigo_x[i] += enemigo_cambio_horizontal[i]

        # Condicional para mantener en los bordes al ENEMIGO
            if enemigo_x[i] <= 0:
                enemigo_cambio_horizontal[i] = 2
                enemigo_y[i] += enemigo_cambio_vertical[i]
            elif enemigo_x[i] >= 736:
                enemigo_cambio_horizontal[i] = -2
                enemigo_y[i] += enemigo_cambio_vertical[i]
        # Colisión
            existe_colision = colision(enemigo_x[i], enemigo_y[i], bala_x, bala_y)
            if existe_colision:
                sonido_colision.play()
                sonido_misil.stop()
                bala_y = pos_y
                bala_visible = False
                enemigo_x[i] = random.randint(0, 736)
                enemigo_y[i] = random.randint(0, 100)
                "Ahora vamos a agregar para que se pueda ver en pantalla"
                puntuaje += 1

        # Llamada del enemigo
            enemigo(enemigo_x[i], enemigo_y[i], i)

        # Actualizar el movimiento de la bala
        if bala_y <= -32:
            bala_visible = False
        if bala_visible:
            disparar_bala(bala_x, bala_y)
            bala_y -= bala_cambio_y

        # Llamada del jugador
        jugador(pos_x, pos_y)

        # Mostrar el puntuaje
        mostrar_puntuacion(texto_x, texto_y)

        # Actualizar lo que estamos viendo en pantalla
        pygame.display.update()
