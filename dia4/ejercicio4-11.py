from random import *
"""ejercicios sobre random"""

"""debemos importar la funcion rand_int, de random, con el * importamos todas las demas de
random de una vez"""
"""el nombre del archivo tampoco debe de ser identico al de alguna funcion que estemos importando,
como por ejemplo random en este caso"""


aleatorio = randint(1, 50)
print(aleatorio)

"""con uniform nos da un numero al azar pero decimal, podemos usar la funcion round si deseamos"""
aleatorio = uniform(1, 50)
print(aleatorio)

edad = [23, 34, 21, 55, 42, 64]
elegir = choice(edad)
print(elegir)

numeros = list(range(0, 50, 5))
shuffle(numeros)
print(numeros)
