"""solucion a 4 ejercicios finales del día 5 pt3"""
# ejercicio 4


def contar_primos(numero):
    primos = []
    for x in range(2, numero+1):
        primos.append(x)

    for i in range(2, numero+1):
        for n in range(2, i):
            if i % n == 0:
                primos.remove(i)
                break
                
    print(primos)


contar_primos(11)
