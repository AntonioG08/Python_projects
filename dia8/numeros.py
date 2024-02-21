def cosmetica():
    for n in range(1, 10000):
        yield f'C - {n}'


def farmacia():
    for z in range(1, 10000):
        yield f'F - {z}'


def perfumeria():
    for x in range(1, 10000):
        yield f'P - {x}'


c = cosmetica()
f = farmacia()
p = perfumeria()


def decorar_funcion(rubro):

    print('------------')
    print('Su turno es: ')
    if rubro == 1:
        print(next(c))
    elif rubro == 2:
        print(next(f))
    elif rubro == 3:
        print(next(p))
    print('Aguarde y será atendido en un momento')
    print('-------------')



