"""Ejercicio sobre crear funciones"""


def mi_funcion(nombre):
    """Funcion para imprimir texto"""
    print(f'Hola mundo soy {nombre}')


mi_funcion('Tony')
print('----------')


def multiplicar(x, y):
    return x*y


resultado = multiplicar(3, 6)
print(resultado)
print('-------')


def sumar(a, b):
    c = a+b
    return c


d = sumar(10, 15)
print(d)
