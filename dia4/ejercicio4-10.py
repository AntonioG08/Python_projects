"""usando las funciones min y max"""

lista = [23, 34, 56, 43, 67, 85, 67]
print(max(lista))
print(min(lista))

"""busca el string de menor denominacion"""
nombre = 'CarlOs'
print(min(nombre.lower()))

dic = {'c1': 34, 'c2': 11}
"""por default buscara el valor minimo de las keys, por ello el c1"""
print(min(dic))
print(min(dic.values()))
