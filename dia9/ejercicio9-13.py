import re
""" Mas ejercicios con busqueda re, pero ahora con busquédas más generales usando 
los caracteres regulares """

texto = 'llama al 833-236-1454 ahora mismo para wash and go'
patron = r'\d\d\d-\d\d\d-\d\d\d\d'

resultado = re.search(patron, texto)
print(resultado)

# En este caso ya no busca un número en específico, busca un patrón de números, independientemente de la combinación
print(resultado.group())
print('--------------')

""" Otros ejemplos de como buscar ahora usando numeradores con los digitos y un compilador que los
divide en bloques """
patron2 = r'\d{3}-\d{3}-\d{4}'

patron3 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado2 = re.search(patron3, texto)
print(resultado2.group(1))
print(resultado2.group(2))
print(resultado2.group(3))
print('---------------')


