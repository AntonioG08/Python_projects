from random import *
"""ejercicio de proyecto del día 4"""

"""Solicitamos el nombre al jugador con un input"""
"""La variable con el número aleatorio debe ir fuera del loop, de lo contario se reinicia el valor 
en cada iteracion"""
nombre = input('Por favor dime tu nombre para iniciar el juego: ')
numero_adivinar = randint(1, 100)
vidas = 8
numero_intento = 0

print(f'Okay {nombre}, he pensado en un número entero entre 1 y 100 para que adivines\n'
      f'para ello tienes 8 intentos, exito')
print(numero_adivinar)

"""Mientras las vidas no lleguen a 0, seguiremos preguntando"""
while vidas > 0:
    numero_intento = int(input(f'ingresa un número: '))
    # Caso 1 en donde el número no está en el rango 1-100
    if (numero_intento < 1) and (numero_intento > 100):
        print('Lo siento, ingrese un número entre 1 y 100')
    # Caso 2 en donde el número es menor al aleatorio
    elif numero_intento < numero_adivinar:
        print('El numero ingresado es menor al número elegido por el programa')
    # Caso 3 en donde el número es mayor al aleatorio
    elif numero_intento > numero_adivinar:
        print('El numero ingresado es mayor al número elegido por el programa')
    # Caso 4 en donde el número es igual al aleatorio, ponemos break por que las vidas aun son mayor a 0
    elif numero_intento == numero_adivinar:
        print(f'El numero es correcto, y te quedaron {vidas} vidas')
        break
    vidas -= 1
    print(f'Te quedan {vidas} vidas')

# Si las vidas son menor a 0, se acaba el juego y se pide reiniciar
if vidas == 0:
    print(f'el numero a adivinar era: {numero_adivinar}')
    print('Lo sentimos, agoto sus vidas, reinicie el juego')









