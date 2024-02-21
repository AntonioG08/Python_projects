"""ejercicios sobre enumerador"""

lista = ['a', 'b', 'c']
indice = 0

for i in lista:
    print(indice, i)
    indice += 1

print('-------')

for x in enumerate(lista):
    print(x)

for z, y in enumerate(lista):
    print(z, y)

print('--------')
mi_tupla = list(enumerate(lista))
print(mi_tupla)

print('--------')

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, x in enumerate(lista_nombres):
    nombre = x
    print(f'{nombre} se encuentra en el índice {indice}')