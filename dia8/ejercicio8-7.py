""" ejercicios sobre decoradores pt3 """


def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion


def mayusculas(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())


""" Con esto podemos tener la funcion mayuscula normal, y además la función mayuscula decorada """
mayuscula_decorado = decorar_saludo(mayusculas)
mayuscula_decorado('tony gomez')
print('------------')
mayusculas('tony gomez')
