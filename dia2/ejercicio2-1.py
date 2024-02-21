x = 85
print(x)
y = 5.5
print(y)

var1 = 45
print(f'var1 primero es un integer de valor {var1}')
"""Podemos cambiar el tipo de dato, por ejemplo el 45 que es integer, a que sea un string de texto"""
var2 = str(var1)
print(f'Pero ahora var2, basado en var1 es un {type(var2)} de valor {var2}')

"""También podemos hacer que el 45 pase de ser un integer a ser un float, aun que no tenga decimales y 
sea solo '45.0' """
print(f'Aun que también podemos convertir el mismo integer de var1, en un {type(float(var1))} con {float(var1)}')

print('---------------')

print(type(x))
print(type(y))
print(type(var2))


