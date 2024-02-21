"""ejercicios sobre tuppers o tuplas"""

"""pueden ir sin el paréntesis y son inmutables, cuando se escribe no puede modificarse"""
mi_tupla = ('perro', 'gato', 'pez')
print(type(mi_tupla))

"""ocupan menos espacio de memoria y son más rápidos de correr"""
"""podemos usarlas en un escenario donde no queremos el riesgo de un cambio de datos"""
tupla2 = (2,3,4,5)
tupla3 = (8, 10.55, 'hola')

print(tupla2[0])

"""los tuples no soportan asignacion de items igual que los strings"""
tupla4 = (1,2,3,(4,5),6)
print(tupla4[3][0])

"""podemos cambiar el tipo"""
tupla3 = list(tupla3)
print(type(tupla3))

"""podemos asignarlo, pero siempre debe coincidir la cantidad de valores y variables"""
n = (1, 2, 3)
x, y, z = n
print(x, y, z)

p = (1,2,3,4,1,5,6,1)
"""con esto contamos el numero de veces que hay 1"""
print(p.count(1))
"""con esto pedimos saber en que numero de indice esta el valor 3"""
print(p.index(3))