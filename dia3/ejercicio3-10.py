"""Ejercicios para prácticar sobre los sets"""

"""Los sets solo tienen valores únicos, no se pueden repetir. Si se repiten 
python los elimina directamente. También no pueden incluir listas o diccionarios"""
mi_set = set(['a', 'b', 'c'])
print(mi_set)
print(type(mi_set))

mi_set2 = {1,2,3,1,4,6,2,3,5,4,3,1,3,2,3,4}
print(mi_set2)
print(type(mi_set2))

"""Ejemplo de unión de sets"""
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
"""Con este método agregamos el valor 6"""
s3.add(6)
print(s3)
"""Con este método quitamos el valor 2"""
s3.remove(2)
print(s3)
"""Con pop eliminamos un elemento, pero al no tener orden los sets, borra el primero"""
s3.pop()
print(s3)
