"""ejercicio sacar valores Y de Kinesis """

mi_archivo = open('kinesis42.txt', 'r')
mi_archivo2 = open('kinesis_ValY.txt', 'a')


for n in mi_archivo:
    texto = n[15:35]
    mi_archivo2.write('\n' + texto)

mi_archivo.close()
mi_archivo2.close()