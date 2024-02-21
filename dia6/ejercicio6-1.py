""" ejercicio de pruebas de abrir archivos de texto"""

mi_archivo = open('prueba1.txt')
mi_archivo2 = open('prueba1.txt')
mi_archivo3 = open('prueba1.txt')

print(mi_archivo.read())
print('--------')
# Con el comando read line leemos 1 linea de texto, y se va en orden una por una
print(mi_archivo2.readline())
print(mi_archivo2.readline())
print('---------')

# Con el comnando rstrip() quitamos el salto de línea del bloc de notas que se genera por el "enter"
# Al commando podemos aplicarle tambien los metodos de strings
linea1 = mi_archivo3.readline()
linea2 = mi_archivo3.readline()
print(linea1.rstrip())
print(linea2)

mi_archivo.close()
mi_archivo2.close()
mi_archivo3.close()

