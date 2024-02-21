import os
import shutil
""" Ejemplos ahora usando OS y Shutil """

# Esto es usando los métodos de importat 'OS'
print(os.getcwd())
"""
Ejemplo de como crear un archivo de texto
archivo = open('curso.txt', 'r')
"""

"""
archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
print('--------')
print(os.listdir())
archivo.close()
"""

# Ahora veremos como hacerlo usando el método 'SHUTIL'
""" Originalmente el archivo 'curso.txt' se habia creado en este sitio, pero ahora se movio a la 
carpeta del día 8 """

shutil.move('curso.txt', 'C:\\Users\\togor\\Documents\\Certificados\\Python total\\Python\\dia8')

# shutil.rmtree()
""" La función de arriba borrará todo lo que le pasemos en una dirección, tiene mas poder que 
remove() y rmdir() del modulo 'OS' """
