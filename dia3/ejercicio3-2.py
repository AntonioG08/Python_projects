"""Usando la tecnica slicing podremos jalar palabras enteras de un enunciado """
texto = 'El dia es muy soleado'
var = texto[3:6]
print(type(var))

"""jala todo de index 6 al ultimo index"""
var2 = texto[6:]

"""Jala todo desde index 0 a index 7"""
var3 = texto[:7]

"""Esta funcion nos retorna la cadena de strings pero leída de derecha a izq"""
var4 = texto[::-1]
print(var)
print(var2)
print(var3)
print(var4)
