"""ejercicios sobre while """

vidas = 3
while vidas > 0:
    print('sigo jugando')
    vidas -= 1

"""usando la funcion 'pass' podemos dejar el lugar apartado, si aun no sabemos
con que llenarlo """
while vidas > 0:
    pass

"""al cumplirse esta condicion, se sale del ciclo while """
nombre = input('Introduce tu nombre: ').lower()
for letra in nombre:
    if letra == 'l':
        break
    print(letra)

nombre2 = input('Introduce tu nombre: ').lower()
for letra2 in nombre:
    """al cumplirse esta condicion, se brinca la letra l y se sigue de largo """
    if letra2 == 'l':
        continue
    print(letra2)

"""NO OLVIDAR, la funcion DO WHILE, que correra el código al menos 1 vez """

numero = 50
while numero >= 0:
    if (numero % 5) == 0:
        print(numero)
    numero -= 1

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for n in lista_numeros:
    if n >= 0:
        print(n)
    elif n < 0:
        break
