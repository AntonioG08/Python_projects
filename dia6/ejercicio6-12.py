"""ejercicio sacar valor tiempo de Kinesis """

mi_archivo = open('kinesis42.txt', 'r')
mi_archivo2 = open('kinesis_Tiempo.txt', 'a')


for n in mi_archivo:
    texto = n[1:12]
    mi_archivo2.write('\n' + texto)

mi_archivo.close()
mi_archivo2.close()
