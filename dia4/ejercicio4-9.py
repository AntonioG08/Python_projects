"""ejercicios sobre la funcion zip"""

nombre = ['tony', 'raul', 'pedro']
edad = [23, 24, 25]

combinar = zip(nombre, edad)
print(combinar)
"""debemos usar el argumento zip para poder ver bien el tuple"""
combinar = list(zip(nombre, edad))
print(combinar)

ciudad = ['tampico', 'queretaro', 'guanajuato']
combinar = list(zip(nombre, edad, ciudad))
print(combinar)


for nombre, edad, ciudad in combinar:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')