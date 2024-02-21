"""Siguen los ejercicios de textos"""

# Podemos hacer recorridos, los cuales son por líneas
archivo1 = open('prueba1.txt')
archivo2 = open('prueba1.txt')

for n in archivo1:
    print('Aqui dice: ' + n)
print('--------')

todas = archivo2.readlines()
print(todas)

archivo1.close()
archivo2.close()

"""
archivo = open('texto.txt')

lineas = (archivo.readlines())
print(lineas[1])

archivo.close()
"""