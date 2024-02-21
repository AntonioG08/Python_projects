"""Ejercicio de prueba de diccionarios"""

dic = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print((dic['c2'][1]).upper())

"""Metodo para agregar datos a un diccionario"""
dic2 = {1: 'a', 2: 'b'}
dic2[3] = 'c'
print(dic2)
"""este metodo cambia el valor del indice 2 de b minuscula a B mayuscula"""
dic2[2] = 'B'
print(dic2)

"""con esto imprimimos las direcciones del diccionario"""
print(dic2.keys())
"""con esto imprimimos los valores que hay en el diccionario"""
print(dic2.values())
"""con esto imprimimos los items del diccionario"""
print(dic2.items())