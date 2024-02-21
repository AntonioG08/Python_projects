"""mas ejercicios sobre ciclo for"""
palabra = 'mexico'
for i in palabra:
    print(i)

for n in 'python':
    print(n)

for objeto in [[1, 2], [3, 4], [5, 6]]:
    print(objeto)

"""en este caso x almacena el item 1 de la sublista, y Y itera el item 2 de la sublista"""
for x, y in [[1, 2], [3, 4], [5, 6]]:
    print(x)
    print(y)

dic = {'clave1': 'a', 'clave2': 'b'}
"""aqui por default solo imprimimos las claves"""
for a in dic:
    print(a)
"""aqui solicitamos imprimir el item completo, tambien podriamos usar '.key' o '.value' """
for b in dic.items():
    print(b)
"""aqui almacenamos los datos en distinas variables, en este caso 'c' y 'd' """
for c, d in dic.items():
    print(c, d)