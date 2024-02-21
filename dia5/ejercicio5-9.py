"""Solucion a 4 ejercicios finales del día 5"""
# ejercicio 1


def devolver_distintos(x, y, z):
    suma = x + y + z
    lista = [x, y, z]
    if suma > 15:
        print(max(lista))
    elif suma < 10:
        print(min(lista))
    else:
        lista.sort()
        print(lista[1])


devolver_distintos(2, 5, 6)
print('--------')
# Ejercicio 2


def tony(palabra):
    palabra2 = palabra.lower()
    palabra2 = list(set(list(palabra2)))
    palabra2.sort()
    print(palabra2)


tony('Holaaaa')
print('---------')



