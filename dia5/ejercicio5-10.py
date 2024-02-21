"""Solucion a 4 ejercicios finales del día 5 pt2"""
# Ejercicio 3


def ceros(*numeros):
    contador = 0
    for x in numeros:
        if contador + 1 == len(numeros):
            return False
        elif numeros[contador] == 0 and numeros[contador+1] == 0:
            return True
        else:
            contador += 1
    return False


print(ceros(1, 5, 3, 0, 3, 5, 7, 6, 0))
print(ceros(1, 5, 3, 0, 0, 3, 5, 7, 6))
print('----------')
"""Tiene un problema, ya que si el 0 es el ultimo valor, arroja tupla fuera de rango"""
"""se arreglo poniendo el primer if"""


def ceros2(*valores):
    cuenta = 0
    for n in valores:
        if n == 0:
            cuenta += 1
        if n != 0:
            cuenta = 0
        elif cuenta == 2:
            return True
    return False




print(ceros2(2, 3, 4, 2, 5, 6, 7, 4, 3))
print(ceros2(2, 3, 4, 0, 0, 2, 5, 6, 7, 4, 3))
print('---------')