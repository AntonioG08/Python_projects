from random import *

"""Proyecto del día 5"""
# Juego del ahorcado
print('Jugaremos al juego del ahorcado, tienes 6 vidas')


def ahorcado():
    palabras = ['tiburon', 'rojo', 'lapiz', 'barco', 'ballena', 'biomedica']
    vidas = 6
    palabra_elegida = choice(palabras)
    lineas = []
    letras_correctas = []

# Con este for haremos la primera barra de lineas para mostrar la longitud de la palabra
    for n in palabra_elegida:
        lineas.append('-')
    print(palabra_elegida)
    print(lineas)

# Con el while, nos aseguraremos que solo jugaremos mientras tengamos vidas restantes
    while vidas > 0:
        lineas = []
        print(f'te quedan {vidas} vidas')
        print('\n')
        letra = input('Elige una letra a adivinar: ').lower()

        if letra in palabra_elegida:
            letras_correctas.append(letra)
        else:
            vidas -= 1

        for n in palabra_elegida:
            if n in letras_correctas:
                lineas.append(n)
            else:
                lineas.append('-')
        print(lineas)
        if lineas == list(palabra_elegida):
            print('Felicidades, ganaste')
            return True

    if vidas == 0:
        print('\n')
        print('Lo sentimos, te haz quedado sin vidas')


ahorcado()
