""" ejercicios sobre generadores pt2 """


def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


g = mi_generador()
print(next(g))
print(next(g))
print('hola mundo')
print(next(g))

""" Ejercicio de generador infinito, ejemplos y soluciones  """


def infinito():
    x = 0
    while True:
        x += 1 
        yield x


def multiplos():
    n = 0
    while True:
        n += 7
        yield n


def multiplos_siete():
    num = 1
    while True:
        yield 7 * num
        num += 1

