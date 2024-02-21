"""ejercicio de comprension de listas"""

"""con este metodo ahorramos lineas en vez de usar el metodo tradicional"""
palabra = 'python'
lista = [letra for letra in palabra]
print(lista)

"""es lo mismo, pero ahorramos otra linea"""
nombre = [x for x in 'python']
print(nombre)

numeros = [y for y in range(0, 21, 2)]
print(numeros)

numeros = [y for y in range(0, 21, 2) if ((y*2) > 10)]
print(numeros)

"""ejercicio de hacer conversion pies a metros"""
pies = [10, 15, 20, 25]
metros = [p * 3.281 for p in pies]
print(metros)
