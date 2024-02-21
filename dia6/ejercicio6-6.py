from pathlib import Path
"""Abrir archivos sin el metodo os"""

# Metodo 1
archivo = open('C:\\Users\\togor\\Documents\\Certificados\\Python total\\Texto_prueba_dia6.txt', 'r')
print(archivo.read())
print('----------')

# Metodo 2, con este metodo nos aseguramos que el código sea legible por cualquier sistema
# Por ejemplo Windos, IOS, Linux, cualquiera puede usar el sistema del path
carpeta = Path('C:/Users/togor/Documents/Certificados/Python total') / 'Texto_prueba_dia6.txt'
archivo2 = open(carpeta)
print(archivo2.read())

