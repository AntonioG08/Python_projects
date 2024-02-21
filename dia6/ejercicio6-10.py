""" ejercicio para prueba UNAM """

mi_archivo = open('prueba1.txt', 'r')
mi_archivo2 = open('prueba3.txt', 'a')


for n in mi_archivo:
    texto = n[0:5]
    mi_archivo2.write('\n' + texto)

mi_archivo.close()
mi_archivo2.close()