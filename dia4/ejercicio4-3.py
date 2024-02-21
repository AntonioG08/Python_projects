"""ejercicios del ciclo for"""

"""imprimir el indie de una lista"""
numeros = [1, 2, 3, 4, 5]
for i in numeros:
    indice_num = numeros.index(i)
    indice_num2 = numeros.index(i) +1
    print(f'numero: {i}, el indice es {indice_num}, y el indice "normal" es {indice_num2}')

letras = ['a', 'b', 'c', 'd']
for n in letras:
    print(f'letra: {n}')

nombres = ['tony', 'arturo', 'luis', 'trevor']
for x in nombres:
    if x.startswith('t'):
        print(x)