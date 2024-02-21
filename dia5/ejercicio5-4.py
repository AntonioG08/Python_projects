"""mas ejercicios sobre listas"""


def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(1, 1000):
            suma += numero
        else:
            pass
    return suma


lista_numeros2 = [1, 50, 500, 5000, 750, 600]
print(suma_menores(lista_numeros2))