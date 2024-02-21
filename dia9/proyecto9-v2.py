""" Segunda parte del proyecto después de descomprimir y leer las instrucciones """
import re
import os
import time
import datetime
from pathlib import Path
import math

ruta = '\\Users\\togor\\Documents\\Certificados\\Python total\\Proyecto_dia9\\Mi_Gran_Directorio'
patron = r'N\D{3}-\d{5}'
# Otra opcion de patron sería r'N\D\D\D-\d\d\d\d\d' lo cual lo vuelve algo largo, ineficiente y confuso
hoy = datetime.date.today()
num_hallados = []
arch_hallados = []

# Variable para medir el tiempo que le tomo al código terminar, esto mide el inicio del tiempo
inicio = time.time()


def buscar_num(archivo, patron2):
    este_arch = open(archivo, 'r')
    texto = este_arch.read()
    if re.search(patron2, texto):
        return re.search(patron2, texto)
    else:
        return ''


def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_num(Path(carpeta, a), patron)
            if resultado != '':
                num_hallados.append((resultado.group()))
                arch_hallados.append(a.title())


def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de búsqueda: {hoy.day}/{hoy.month}/{hoy.year}\n')
    'si ponemos solo {hoy} nos imprimira por ejemplo 2023-09-08, y nosotros queremos dia-mes-año'
    print('Archivo\t\t\tNo. Serie')
    print('-------\t\t\t---------')
    for a in arch_hallados:
        print(f'{a}\t{num_hallados[indice]}')
        indice += 1
    print('\n')
    print(f'Numeros encontrados: {len(num_hallados)}')
    'Variable para finalizar el conteo del tiempo'
    fin = time.time()
    duracion = fin - inicio
    if math.ceil(duracion) == 1:
        'Usamos math.ceil para un redondeo hacía arriba, ya que ceil significa techo'
        print(f'Duración de la búsqueda: {math.ceil(duracion)} segundo')
    else:
        'Usamos math.ceil para un redondeo hacía arriba, ya que ceil significa techo'
        print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)


crear_listas()
mostrar_todo()

"""Aprendido: Vimos bibliotecas integradas, como usar 'collections' para trabajar con diccionarios, estructuras, et. 
también usamos el módulo OS, time y timedate para medir la duracion que le toma a los bloques de código ejecutarse. 
el módulo date/time también nos ayudo para poner en nuestros códigos el día actual en el que estamos. Luego usando 
estructuras pudimos hacer búsquedas específicas en los códigos, e incluso dentro de carpteas, subcarpetas y archivos
para hallar todo esto."""