from collections import namedtuple
""" Ejercicio ahora con tupla 'nombrada' """

mi_tupla = (300, 56, 69)
print(mi_tupla[0])

""" En caso de que la tupla sea muy grande, y ya halla olvidado los valores, o no quiera buscar por el numero
de indice, podríamos buscarlo por el nombre del objeto que contiene """
print('-' * 10)

Persona = namedtuple('persona', ['nombre', 'altura', 'peso'])
Tony = Persona('Tony', '175', '85')
print(Tony.nombre)
print(Tony.altura)
print('-' * 10)
print(Tony[2])