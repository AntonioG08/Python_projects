"""ejercicios con match (lo que yo conocia como 'cases') """

"""ejemplo sin match"""
serie = 'N02'
if serie == 'N01':
    print('motorola')
elif serie == 'N02':
    print('apple')
elif serie == 'N03':
    print('huawei')
else:
    print('nokia')

serie1 = input('ingrese un numero de serie: ').upper()
"""ejemplo con match"""
match serie1:
    case 'M01':
        print('Celular')
    case 'M02':
        print('laptop')
    case 'M03':
        print('ipod')
    case _:
        print('no existe')

print('---------')
"""ejercicio 2 con match"""
cliente = {'nombre': 'Tony',
           'edad': 23,
           'ocupacion': 'estudiante'}

pelicula = {'titulo': 'titanic',
            'ficha tecnica': {'protagonista': 'kate winslet',
                              'director': 'james cameron'}}

elemento = [cliente, pelicula, 'libros']

for e in elemento:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print('es un cliente')
            print(f'{nombre} tiene {edad} y es {ocupacion}')
        case {'titulo': titulo,
              'ficha tecnica': {'protagonista': protagonista,
                                'director': director}}:
            print('--------')
            print('esto es una pelicula')
            print(f'la pelicula {titulo} tiene a {protagonista} como protagonista y a {director} como director')
        case _:
            print('--------')
            print('no se que es esto')

