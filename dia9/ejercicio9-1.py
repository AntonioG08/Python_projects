from collections import Counter
""" Primer ejercicio sobre collections """
""" Counter
    Default 
    namedtuple """

numeros = (8, 8, 7, 5, 34, 7, 3, 7, 3, 7, 4, 2, 3, 2)
print(Counter(numeros))
print('--------')
print(Counter('mississippi'))
print('---------')
frase = 'al pan pan y al vino vino'
print(Counter(frase.split()))
print('---------')
serie = Counter([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4])
""" Nos imprimira en orden de los valores que sean del mas frecuente al menos """
print(serie.most_common())
print('---------')
""" Con esto ahora imprimiremos los 2 más repetidos"""
print(serie.most_common(2))

