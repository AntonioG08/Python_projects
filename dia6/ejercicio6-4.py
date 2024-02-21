import os
""" Buscar archivos en una ruta distinta """

# Buscamos el archivo con la direccion completa
# CWD es Current Working Directory
ruta = os.getcwd()
print(ruta)

# Con esto hemos cambiado la direccion actual, ahora ya nos movimos a otro directorio
ruta2 = os.chdir('C:\\Users\\togor\\Documents\\Certificados\\Python total')
archivo = open('Texto_prueba_dia6.txt')
print(archivo.read())

# Con esto estamos creando una carpeta nueva que no existia
"""
ruta2 = os.makedirs('C:\\Users\\togor\\Documents\\Certificados\\Python total\\nueva')
"""