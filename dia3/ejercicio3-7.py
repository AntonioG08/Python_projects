"""Ejercicios para entender los diccionarios"""

"""Las claves no pueden repetirse"""
dicc1 = {'valor': 4, 'valor2': 8}
print(dicc1)
print(type(dicc1))

x = dicc1['valor']
print(x)

cliente = {'nombre': 'Tony', 'edad': 23, 'peso': 85}

"""ejemplo de un diccionario que contiene una lista y otro diccionario adentro"""
dicc2 = {'c1': 3, 'c2': ['a', 'b', 'c'], 'c3': {'s1': 100, 's2': 200}}
"""Con esto imprimo la lista c2 del diccionario"""
print(dicc2['c2'])
"""Con esto imprimo el indice 1 de la lista c2 del diccionario"""
print(dicc2['c2'][1])
"""Con esto imprimo el valor S2 del diccionario C3 contenido en el diccionaro dicc2 """
print(dicc2['c3']['s2'])