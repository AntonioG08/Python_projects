"""Ejercicios de listas"""
lista = ['a', 'b', 'c', 'd']
lista2 = ['e', 'f', 'g', 'h']
print(type(lista))

"""Funcion longitud de lista"""
print(len(lista))

"""imprime indice 0 de la lista"""
x = lista[0]
print(x)

"""imprime indice 0 y 1 de lista"""
y = lista[0:2]
print(y)


"""En este caso las listas no fueron modificadas, solo se sumaron al imprimirse"""
print(lista + lista2)

lista3 = lista + lista2
lista3[0] = "hola"
print(lista3)
lista3.append('m')
print(lista3)


lista5 = ['x', 'y', 'z']
print(lista5)
"""Con la función pop en blanco se elimina el último indice"""
lista5.pop()
print(lista5)
"""En la función pop dentro del paréntesis podemos elegir que indice eliminar"""
lista5.pop(0)
print(lista5)

lista6 = ['l', 'm', 'n']
"""Con este metodo podemos almacenar la variable que eliminamos de la lista"""
eliminado = lista6.pop()
print(eliminado)

