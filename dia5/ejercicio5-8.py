"""Ejercicio con *kwargs """


def suma(**kwargs):
    print(type(kwargs))


suma(x= 2, y= 5, z= 3)
# No le estoy dando parametros de un diccionario, sin embargo al pasar por el argumento arroja uno
print('-------')


def suma2(**kwargs2):
    total = 0
    for clave,valor in kwargs2.items():
        print(f'Clave es igual a {clave} con valor {valor}')
        total += valor
    return total


print(suma2(x= 5, y= 4, z= 8))
print('-------')

# El orden es primero numeros, luego args y al final kwargs
def prueba(num1, num2, *args, **kwargs3):
    print(f'El valor 1 es {num1}')
    print(f'El valor 2 es {num2}')

    for x in args:
        print(f'valor = {x}')

    for clave,valor in kwargs3.items():
        print(f'Clave es igual a {clave} con valor {valor}')


"""Otro metodo que podriamos usar es:
args = [1,2,3,4,5]
kwargs = [x=2, y=4, z=8]
al invocar la funcion seria de la siguiente forma:
prueba(9,4, *args, **kwargs)"""
prueba(9, 4, 35, 23, 45, 86, 365, 7433, x='uno', y='dos')
print('-------')


def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}:')
    for x, y in kwargs.items():
        print(f'{x}: {y}')