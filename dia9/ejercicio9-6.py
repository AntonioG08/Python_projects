import send2trash
import os
""" Ejercicios de prueba del modulo 'send2trash' """

# A diferencia de los modulos OS y SHUTIL, esto al borrar lo manda a la papelera, los otros desaparecen por completo
"""
send2trash.send2trash('curso.txt')
"""

# Ejemplo para hacer un recorrido entero en una direccion dada
"""
print(os.walk('Pegar ruta de la carpeta que queremos recorrer totalmente'))
"""
""" De momento no hara nada pues solo se creo la 'orden' o la 'instruccion' por asi decirlo, esto 
podemos ponerlo en un iterador y que ahora si inice a recorrerlo"""

ruta_ejemplo = 'C:\\Users\\togor\\Documents\\Certificados\\Python total\\Python\\dia8'

for carpeta, subcarpeta, archivo in os.walk(ruta_ejemplo):
    print(f'En la carpeta {carpeta}')
    print('Las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son: ')
    for doc in archivo:
        print(f'\t{doc}')
        """
        if doc.startswith('ejercicio'):
            print(f'\t{doc}')
        Con esa funcion podemos filtrar que archivos queremos que se muestren en caso de tener muchos
        """
    print('\n')
