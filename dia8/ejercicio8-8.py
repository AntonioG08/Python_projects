""" Ejercicio sobre generadores """
""" función generadora """
""" en vez de crear un código que almacene una lista con muchas variables, podemos 
tener una función generadora que vaya creándola conforme la necesitemos. De 
esta manera no tendremos tanto espacio en la memoria ocupado """

"""Función normal"""


def mi_funcion():
    return 4


def mi_generador():
    yield 4


""" No va a imprimir el 4 por que no se ha creado a diferencia de 'mi_funcion', hasta que sea invocada
ya existirá el 4 tal cual """
print(mi_funcion())
print(mi_generador())
print('---------')

g = mi_generador()
print(next(g))
print('---------')
print('---------')


def mi_funcion2():
    lista = []
    for n in range(1, 5):
        lista.append(n * 10)
    return lista


def mi_generador2():
    for x in range(1, 5):
        yield x * 10


print(mi_funcion2())
print('---------')

g2 = mi_generador2()
print(next(g2))
print(next(g2))


