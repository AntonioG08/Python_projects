from os import system
from pathlib import *
""" proyecto del día 6 """
"""Autor Antonio Gómez Ruiz, Mayo 2023"""
# carpeta = Path('C:\Users\togor\Recetas')

num_recetas = 0
guia1 = Path(Path.home(), 'Recetas')
eleccion = 0


def inicio():
    print('¡Saludos usuario!')
    print(f'La dirección del recetario es: {guia1}')


def revisar_direccion():
    cantidad = 0
    categoria1 = ''
    carpetas = []
    for x in Path(guia1).glob('*'):
        carpetas.append(x.name)
    print('Las categorias de recetas que tiene son las siguientes: ')

    for n in carpetas:
        """print('- ' + n)"""
        categoria1 = n
        guia2 = Path(Path.home(), 'Recetas', categoria1)
        for m in Path(guia2).glob('*.txt'):
            cantidad += 1

    print(f'Actualmente tiene {cantidad} recetas entre todas sus categorias')


def elegir():
    print('¿Que desea hacer?')
    print('1 leer receta\n2 Crear receta\n3 Crear categoria\n4 Eliminar receta\n5 Eliminar categoria\n6 Salir')
    opcion = int(input('¿Que opcion desea elegir?: '))
    return opcion


def leer_receta():
    op = 1
    carpetas = []
    recetas = []
    system('cls')
    print('Primero comenzemos por elegir una categoria')
    for x in Path(guia1).glob('*'):
        carpetas.append(x.name)
    print('Las categorias de recetas que tiene son las siguientes: ')
    for n in carpetas:
        print(f'{op}  {n}')
        op += 1
    num = input('Ingrese el numero de la categoria que desea abrir: ').lower()

    if num == 'carnes':
        system('cls')
        val = 1
        categoria2 = carpetas[0]
        guia3 = Path(Path.home(), 'Recetas', categoria2)

        print(f'Las recetas en {categoria2} son las siguientes: ')
        for p in Path(guia3).glob('*.txt'):
            recetas.append(p.stem)
        for k in recetas:
            print(f'{val} {k}')
            val += 1
        print('Elija 1 si desea continuar y elegir una receta')
        opcion2 = int(input('Elija 2 si desea regresar al inicio \nIngrese su opcion: '))
        if opcion2 == 1:
            eleccion2 = int(input('Elija el numero de receta que desea: '))
            receta_elegida = recetas[eleccion2-1]
            receta_elegida2 = (receta_elegida + '.txt')
            archivo = Path(Path.home(), 'Recetas', categoria2, receta_elegida2)
            system('cls')
            print(archivo.read_text())
            fin = input('Teclee Enter para volver al menu principal')
            return
        if opcion2 == 2:
            system('cls')
            return

    if num == 'ensaladas':
        system('cls')
        val = 1
        categoria2 = carpetas[1]
        guia3 = Path(Path.home(), 'Recetas', categoria2)

        print(f'Las recetas en {categoria2} son las siguientes: ')
        for p in Path(guia3).glob('*.txt'):
            recetas.append(p.stem)
        for k in recetas:
            print(f'{val} {k}')
            val += 1
        print('Elija 1 si desea continuar y elegir una receta')
        opcion2 = int(input('Elija 2 si desea regresar al inicio \nIngrese su opcion: '))
        if opcion2 == 1:
            eleccion2 = int(input('Elija el numero de receta que desea: '))
            receta_elegida = recetas[eleccion2-1]
            receta_elegida2 = (receta_elegida + '.txt')
            archivo = Path(Path.home(), 'Recetas', categoria2, receta_elegida2)
            system('cls')
            print(archivo.read_text())
            fin = input('Teclee Enter para volver al menu principal')
            return
        if opcion2 == 2:
            system('cls')
            return

    if num == 'pastas':
        system('cls')
        val = 1
        categoria2 = carpetas[2]
        guia3 = Path(Path.home(), 'Recetas', categoria2)

        print(f'Las recetas en {categoria2} son las siguientes: ')
        for p in Path(guia3).glob('*.txt'):
            recetas.append(p.stem)
        for k in recetas:
            print(f'{val} {k}')
            val += 1
        print('Elija 1 si desea continuar y elegir una receta')
        opcion2 = int(input('Elija 2 si desea regresar al inicio \nIngrese su opcion: '))
        if opcion2 == 1:
            eleccion2 = int(input('Elija el numero de receta que desea: '))
            receta_elegida = recetas[eleccion2-1]
            receta_elegida2 = (receta_elegida + '.txt')
            archivo = Path(Path.home(), 'Recetas', categoria2, receta_elegida2)
            system('cls')
            print(archivo.read_text())
            fin = input('Teclee Enter para volver al menu principal')
            return
        if opcion2 == 2:
            system('cls')
            return

    if num == 'postres':
        system('cls')
        val = 1
        categoria2 = carpetas[3]
        guia3 = Path(Path.home(), 'Recetas', categoria2)

        print(f'Las recetas en {categoria2} son las siguientes: ')
        for p in Path(guia3).glob('*.txt'):
            recetas.append(p.stem)
        for k in recetas:
            print(f'{val} {k}')
            val += 1
        print('Elija 1 si desea continuar y elegir una receta')
        opcion2 = int(input('Elija 2 si desea regresar al inicio \nIngrese su opcion: '))
        if opcion2 == 1:
            eleccion2 = int(input('Elija el numero de receta que desea: '))
            receta_elegida = recetas[eleccion2-1]
            receta_elegida2 = (receta_elegida + '.txt')
            archivo = Path(Path.home(), 'Recetas', categoria2, receta_elegida2)
            system('cls')
            print(archivo.read_text())
            fin = input('Teclee Enter para volver al menu principal')
            return
        if opcion2 == 2:
            system('cls')
            return


while eleccion != 6:
    system('cls')
    inicio()
    revisar_direccion()
    eleccion = elegir()

    if eleccion == 1:
        leer_receta()









