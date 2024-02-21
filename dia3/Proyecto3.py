"""Código para hacer el proyecto de la leccion 3"""
texto = (input('Ingresa un enunciado el cual va a ser analizado: '))
texto = texto.lower()


"""funcion para solicitar al usuario 3 letras y almacenarla en variables minusculas"""
print('Ahora ingrese 3 letras de su eleccion porfavor')
x = input('ingrese la primera: ').lower()
y = input('ingrese la segunda: ').lower()
z = input('ingrese la tercera: ').lower()


"""3 funciones para contar las 3 letras elegidas por el usuario en el texto"""
cuentax = 0
for i in texto:
    if i == x:
        cuentax += 1
print(f'La letra {x} aparece {cuentax} veces en el texto')
cuentay = 0
for i in texto:
    if i == y:
        cuentay += 1
print(f'La letra {y} aparece {cuentay} veces en el texto')
cuentaz = 0
for i in texto:
    if i == z:
        cuentaz += 1
print(f'La letra {z} aparece {cuentaz} veces en el texto')


"""funcion para contar el numero de palabras en el texto"""
palabras = texto.split(' ')
print(f'El numero de palabras en el texto es {len(palabras)}')


"""Funcion para decir la primera y ultima letra"""
print(f'La primera letra del texto es {texto[0]}')
print(f'La ultima letra del texto es {texto[-1]}')


"""Funcion para imprimir el texto ingresado en reversa"""
palabras.reverse()
texto_reversa1 = ' '.join(palabras)
print("El texto al reves sería: " + texto_reversa1)


"""Funcion para imprimir si python existe en el texto"""
if 'python' in texto:
    print('Python existe en el texto')
else:
    print('python no existe en el texto')