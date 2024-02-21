"""ejercicio de funciones con loop y tuples"""

cafe_precios = [('americano', 2), ('mexicano', 1.5), ('frances', 3)]
for elemento in cafe_precios:
    print(elemento)
print('--------')
for x, y in cafe_precios:
    print(x, y)
print('--------')


def cafe_caro(m):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe, precio in m:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return cafe_mas_caro, precio_mayor


res1, res2 = cafe_caro(cafe_precios)
print(f'el cafe mas caro es {res1} con un valor de {res2}')