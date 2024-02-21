import os
from os import system
from pathlib import *
""" proyecto del día 6 """
"""Autor Antonio Gómez Ruiz, Mayo 2023"""
# Este es el path.home() carpeta = Path('C:\Users\togor\Recetas')

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
    num = int(input('Ingrese el numero de la categoria que desea abrir: '))

    val = 1
    categoria2 = carpetas[num-1]
    guia3 = Path(Path.home(), 'Recetas', categoria2)
    system('cls')
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
        receta_elegida = recetas[eleccion2 - 1]
        receta_elegida2 = (receta_elegida + '.txt')
        archivo = Path(Path.home(), 'Recetas', categoria2, receta_elegida2)
        system('cls')
        print(archivo.read_text())
        fin = input('Teclee Enter para volver al menu principal: ')

    if opcion2 == 2:
        system('cls')
        return


def crear_receta():
    """Variables a utilizar en la función"""
    system('cls')
    opcion = 1
    carpetas = []

    """Parte de la función donde se elige en que categoría ubicarnos"""
    print('Elija primero la categoría donde desea crear su receta')
    for x in Path(guia1).glob('*'):
        carpetas.append(x.name)
    print('Las categorias de recetas que tiene son las siguientes: ')
    for n in carpetas:
        print(f'{opcion}  {n}')
        opcion += 1
    num = int(input('Ingrese el numero de la categoria que desea elegir: '))
    categoria2 = carpetas[num-1]
    system('cls')
    print(f'Usted esta en la categoría {categoria2}')
    print('Elija 1 si desea continuar y crear una receta')
    opcion2 = int(input('Elija 2 si desea regresar al inicio \nIngrese su opcion: '))

    if opcion2 == 1:
        """Parte de la fución que crea el archivo de texto"""
        system('cls')
        print(f'Usted esta en la categoría {categoria2}')
        titulo = input('Elija un título para su receta: ')
        titulo2 = (titulo + '.txt')
        archivo = Path(Path.home(), 'Recetas', categoria2, titulo2)
        archivo2 = open(archivo, 'w')
        cuerpo = input('Ingrese su receta: ')
        archivo2.write(cuerpo)
        archivo2.close()
        print('Felicidades, ha creado una nueva receta')
        fin = input('Teclee Enter para volver al menú: ')
    if opcion2 == 2:
        system('cls')
        return


def crear_categoria():
    """Variables a utilizar en la función"""
    system('cls')
    opcion = 1
    carpetas = []
    """Parte de la función donde vemos todas las categorias actuales"""
    for x in Path(guia1).glob('*'):
        carpetas.append(x.name)
    print('Las categorias de recetas que tiene son las siguientes: ')
    for n in carpetas:
        print(f'{opcion}  {n}')
        opcion += 1
    print('Elija 1 si desea continuar y crear una categoria')
    opcion2 = int(input('Elija 2 si desea regresar al inicio \nIngrese su opcion: '))

    if opcion2 == 1:
        """Parte de la función que crea la categoria"""
        system('cls')
        opcion = 1
        print('Las categorias de recetas que tiene son las siguientes: ')
        for n in carpetas:
            print(f'{opcion}  {n}')
            opcion += 1
        nombre = input('Ingrese el nombre de la categoría nueva que desea agregar: ')
        archivo = Path(Path.home(), 'Recetas', nombre)
        ruta_nueva = os.makedirs(archivo)
        print(f'Felicidades, la carpeta {nombre} ha sido creada')
        fin = input('Teclee Enter para volver al menú principal: ')
    if opcion2 == 2:
        system('cls')
        return


def eliminar_receta():

    """Variables a utilizar en la función"""
    system('cls')
    opcion = 1
    carpetas = []
    recetas = []
    val = 1

    """Parte de la función donde se elige en que categoría ubicarnos"""
    print('Elija primero la categoría donde desea eliminar su receta')
    for x in Path(guia1).glob('*'):
        carpetas.append(x.name)
    print('Las categorias de recetas que tiene son las siguientes: ')
    for n in carpetas:
        print(f'{opcion}  {n}')
        opcion += 1

    num = int(input('Ingrese el numero de la categoria que desea elegir: '))
    categoria2 = carpetas[num-1]
    guia3 = Path(Path.home(), 'Recetas', categoria2)
    system('cls')
    print(f'Las recetas en {categoria2} son las siguientes: ')
    for p in Path(guia3).glob('*.txt'):
        recetas.append(p.stem)
    for k in recetas:
        print(f'{val} {k}')
        val += 1

    print('Elija 1 si desea continuar y eliminar una receta')
    opcion2 = int(input('Elija 2 si desea regresar al inicio \nIngrese su opcion: '))

    if opcion2 == 1:
        """Parte de la función que elimina la receta"""
        nombre = input('Ingrese el nombre de la receta a eliminar tal cual aparece: ')
        nombre2 = (nombre + '.txt')
        archivo = Path(Path.home(), 'Recetas', categoria2, nombre2)
        os.remove(archivo)
        print(f'Proceso completado, la receta {nombre} ha sido eliminada')
        fin = input('Teclee Enter para volver al menú principal: ')
    if opcion2 == 2:
        system('cls')
        return


def eliminar_categoria():
    """Variables a utilizar en la función"""
    system('cls')
    opcion = 1
    carpetas = []
    """Parte de la función donde vemos todas las categorias actuales"""
    for x in Path(guia1).glob('*'):
        carpetas.append(x.name)
    print('Las categorias de recetas que tiene son las siguientes: ')
    for n in carpetas:
        print(f'{opcion}  {n}')
        opcion += 1
    print('Elija 1 si desea continuar y borrar una categoria')
    opcion2 = int(input('Elija 2 si desea regresar al inicio \nIngrese su opcion: '))

    if opcion2 == 1:
        """Parte de la función que crea la categoria"""
        system('cls')
        opcion = 1
        print('Las categorias de recetas que tiene son las siguientes: ')
        for n in carpetas:
            print(f'{opcion}  {n}')
            opcion += 1
        nombre = input('Ingrese el nombre de la categoría que desea borrar tal cual aparece: ')
        archivo = Path(Path.home(), 'Recetas', nombre)
        os.rmdir(archivo)
        print(f'Proceso completado, la carpeta {nombre} ha sido eliminada')
        fin = input('Teclee Enter para volver al menú principal: ')
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
    if eleccion == 2:
        crear_receta()
    if eleccion == 3:
        crear_categoria()
    if eleccion == 4:
        eliminar_receta()
    if eleccion == 5:
        eliminar_categoria()
system('cls')
print('Cerrando el programa...')
print('Vuelva pronto!')

