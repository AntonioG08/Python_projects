from random import *
"""ejercicio sobre interaccion entre funciones"""
"""ejercicio de elegir el palito mas largo"""


# Lista inicial
palitos = ['-', '--', '---', '----']


# Mezclar palitos
def mezclar(lista1):
    shuffle(lista1)
    return lista1


# Pedir intento
def probrar_suerte():
    intento = 0
    while intento not in [1,2,3,4]:
        intento = int(input('Elige un numero del 1 al 4: '))
    return intento


# Comprobar intento
def checar_intento(lista, intento):
    if lista[intento-1] == '-':
        print('Te toco el palito mas corto, perdiste')
    else:
        print('Te salvaste')
    print(f'te ha tocado {lista[intento-1]}')


# Con palitos mezclados invocamos la funcion mezclar usando la lista palitos
palitos_mezclados = mezclar(palitos)

# Con seleccion elegimos un numero al azar de 1 a 4
seleccion = probrar_suerte()

# Con esto invocamos la funcion usando los parametros de los palitos mezclados y del numero seleccionado
checar_intento(palitos_mezclados, seleccion)

print ('--------')


def reducir_lista(lista1):
    lista = list(set(lista1))
    lista.sort()
    lista.pop(-1)
    return lista


def promedio(lista):
    valor_prom = sum(lista) / len(lista)
    return valor_prom


lista_numeros = [1, 3, 4, 4, 6, 7, 3, 3, 6, 8]
lista2 = reducir_lista(lista_numeros)
print(lista2)
print(promedio(lista2))
