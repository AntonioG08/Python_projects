"""ejercicios sobre argumentos *args"""

# Cualquier cosa puede ser un argumento siempre que inicie con un *
# Ejemplo, *args, *cos, *num


def suma(*args):
    total = 0

    for x in args:
        total += x
    return total


print(suma(1,4,6,3,8,5,4))
print('--------')


def suma2(*args):

    return sum(args)


print(suma(1,4,6,3,8,5,4))
print('-------')


def suma_absolutos(*args):
    suma3 = 0
    for x in args:
        suma3 += abs(x)
    return suma3
