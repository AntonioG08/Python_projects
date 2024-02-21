import time
import timeit
""" Ejercicios para ver la eficacia de dos funciones que hacen lo mismo, pero estan 
escritas de una manera distinta """


def prueba_for(numero):
    lista = []
    for num in range(1, numero +1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


inicio = time.time()
prueba_for(100000)
final = time.time()
print(final-inicio)

inicio = time.time()
prueba_while(100000)
final = time.time()
print(final-inicio)
print('------------')

mi_declaracion = """
prueba_for2(10)
"""
mi_setup = """
def prueba_for2(numero):
    lista = []
    for num in range(1, numero +1):
        lista.append(num)
    return lista
"""
duracion = timeit.timeit(mi_declaracion, mi_setup, number=1000000)
print(duracion)



