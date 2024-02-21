import re
""" continuamos con ejercicios sobre buscar de manera especifica en claves """

clave = input('Clave : ')
patron = r'\D{1}\w{7}'
chequear = re.search(patron, clave)

print(chequear)
print('-----------')

# Aqui podemos poner que busque lunes Ó martes, muy util en ejemplos en plural por ejemplo
texto = 'No atendemos los lunes por las tardes'
buscar = re.search(r'lunes|martes', texto)
print(buscar)
print('------------')

# Con el siguiente, podemos usar puntos para incluir espacios/caracteres antes y despues de la coincidencia hallada
buscar2 = re.search(r'....demos...', texto)
print(buscar2)
