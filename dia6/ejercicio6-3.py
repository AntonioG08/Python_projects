"""Ejercicios de abrir texto con R, W y A"""

# Cuando no hemos puesto nada, python asume que es solo lectura
archivo = open('prueba1.txt', 'r')
# archivo.write('Este es el nuevo texto')

# Con w el texto es totalmente reemplazado por el nuevo, hay que tener cuidado
archivo2 = open('prueba2.txt', 'w')
archivo2.write('Este es el nuevo texto\n')
archivo2.write('Hola Tony\n')
archivo2.write("""Esta es 
otra manera de saltar""")

# Con a podemos empezar a escribir desde el último caracter sin modificarlo
archivo3 = open('prueba2.txt', 'a')
archivo3.write('\nHola, este es el metodo A')

archivo.close()
archivo2.close()
archivo3.close()

"""
archivo = open('mi_archivo.txt', 'w')
archivo.write('Nuevo texto')
archivo.close()

archivo = open('mi_archivo.txt')
print(archivo.read())
"""