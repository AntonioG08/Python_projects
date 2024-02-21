import datetime

""" Ejercicios con la función de datetime """

# En la función son horas; minutos; segundos; microsegundos. Si no hay nada, se rellena con cero
mi_hora = datetime.time(17, 35)
print(type(mi_hora))
print('-----------')
print(mi_hora)
print('--------------------')

mi_dia = datetime.date(2023, 11, 12)
print(mi_dia.ctime())
print('-----------------')

""" Con la función de abajo, podemos imprimir la fecha actual, reescribiendo en un objeto de fecha ya creado"""
print(mi_dia.today())
print('-----------------')




