from random import *

palabras = ['universidad', 'rojo', 'lapiz', 'barco', 'ballena', 'biomedica']
letras_incorrectas = []
letras_correctas = []
vidas = 6
aciertos = 0
juego_terminado = False

palabra_elegida = choice(palabras)
letras_unicas = len(set(palabra_elegida))


def letra_elegida():
    letra = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra = input('Ingrese una letra por favor: ').lower()
        if letra in abecedario and len(letra) == 1:
            es_valida = True
        else:
            print('No has elegido una letra correcta')
    return letra


def mostrar_tablero(palabra_eleccion):
    lista = []

    for n in palabra_eleccion:






