from numeros import *
from os import *
""" cosmetica, perfumeria, farmacia """
eleccion = 0


def inicio():
    print('!Bienvenido a la tienda!')
    print('Por favor ingrese a continuación el área al que desea acudir para recibir su turno')
    print('1 Cosmética\n2 Farmacia\n3 Perfumería\n4 Salir')
    opcion = int(input('Elija su opcion: '))
    return opcion


while eleccion != 4:
    system('cls')
    eleccion = inicio()
    if eleccion == 4:
        break

    system('cls')
    decorar_funcion(eleccion)
    volver = input('Presione Enter para volver al menú')

system('cls')
print('Programa finalizado con éxito')
print('Gracias, vuelva pronto!')

