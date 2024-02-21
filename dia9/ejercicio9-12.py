import re
""" Ejercicios ya prácticos con el uso del módulo re y las expresiones vistas previamente en 
los ejercicios '9-11' """

texto = 'yo dije que decidi estudiar ingenieria biomedica por que es la mejor ingenieria que existe y es el futuro'

patron = 'fiesta'
busqueda = re.search(patron, texto)
print(busqueda)
print('------------')

patron2 = 'estudiar'
busqueda2 = re.search(patron2, texto)
print(busqueda2)
print(busqueda2.span())
print(busqueda2.start())
print(busqueda2.end())
print('-------------')

patron3 = 'que'
busqueda3 = re.findall(patron3, texto)
print(busqueda3)

# Con este metodo for ahora tenemos la ubicación de las 3 palabras 'que' encontradas en el texto
for encontrar in re.finditer(patron3, texto):
    print(encontrar.span())
