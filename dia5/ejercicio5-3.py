"""Mas ejemplos de funciones"""


def num_3_cifras(x):
    return x in range(100, 1000)


suma = 100+345
resultado = num_3_cifras(suma)
print(resultado)
print('--------')


def num_3_cifras2(lista):

    for n in lista:
        if n in range(100, 1000):
            return True
        else:
            pass
    return False


lista2 = (66, 14, 4000, 124, 324, 8)
y = num_3_cifras2(lista2)
print(y)
print('--------')


def num_3_cifras3(lista3):

    lista_si = []
    lista_no = []
    for p in lista3:
        if p in range(100, 1000):
            lista_si.append(p)
        else:
            lista_no.append(p)
    return lista_si, lista_no


lista4 = (66, 14, 4000, 124, 324, 8)
m, u = num_3_cifras3(lista4)
print(m)
print(u)

