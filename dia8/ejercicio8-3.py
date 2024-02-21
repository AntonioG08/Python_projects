from os import *
"""Ejercicio sobre try, except, finally"""


def pedir_numero():

    while True:

        try:
            numero = int(input('Ingrese un número por favor: '))
        except:
            system('cls')
            print('Usted no ha ingresado un número, trate nuevamente')
        else:
            system('cls')
            print(f'Usted ha ingresado el número {numero}')
            break
    print('Gracias!')


pedir_numero()
