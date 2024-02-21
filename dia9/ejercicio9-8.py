from datetime import *

mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)
print(mi_fecha)
print('--------------')
mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha)

""" función para guardar los minutos de la hora actual leida
from datetime import *
minutos = datetime.now().minute """