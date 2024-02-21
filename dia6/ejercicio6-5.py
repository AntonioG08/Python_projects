import os
"""Ejercicios sobre los directorios"""

ruta = 'C:\\Users\\togor\\Documents\\Certificados\\Python total'

# Imprimimos el elemento final
elemento = os.path.basename(ruta)
print(elemento)
print('---------')
# Imprimimos todo antes del elemento
elemento2 = os.path.dirname(ruta)
print(elemento2)
print('----------')
# Con esto ahora se imprimio pero en una tupla
elemento3 = os.path.split(ruta)
print(elemento3)

# Con esto podemos eliminar una carpeta elegida, tener cuidado con esta funcion
"""
os.rmdir('C:\\Users\\togor\\Documents\\Certificados\\Python total')
"""

