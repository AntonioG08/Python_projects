""" Ejercicios sobre decoradores """

""" La siguiente sintaxis no sería muy util y sería muy repetitiva"""
"""def mayuscula_hola(texto):
    print('hola')
    print(texto.upper())
    print('adios')


def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower()) """


def mayuscula(texto):
    print(texto.upper())


mi_funcion = mayuscula
mi_funcion('python')
print('---------')


def una_funcion(funcion):
    return funcion


una_funcion(mayuscula('tony gomez'))
print('----------')


def cambiar_letras(tipo):

    def mayuscula2(texto):
        print(texto.upper())

    def minuscula2(texto):
        print(texto.lower())

    if tipo == 'mayuscula':
        return mayuscula2
    elif tipo == 'minuscula':
        return minuscula2


operacion = cambiar_letras('mayuscula')
operacion('palabra')
