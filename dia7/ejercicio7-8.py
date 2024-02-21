""" Propiedades de  Programación orientada a objetos tales como:
Herencia - polimorfismo - cohesión - abstracción
acoplamiento - encapsulamiento """

""" Una clase hija puede heredar atributos de una clase padre, modificarlos 
e incluso escribir nuevos atributos """

""" Para la clase hija podemos pasarle los parametros de la clase padre """
""" Podemos crear la clase "VIVO" y heredar a clases como:
pajaro - perro - humano - gato etc, esto por quer todos comparten las carcteristicas de la clase VIVO """

""" Recordar el mantra DRY, 'Dont Repeat Yourself' 
no repetir código de manera innecesaria """


class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('este animal ha nacido')


""" Con esto heredamos nacer a todas las clases que queramos sin tener que repetir código innecesario"""
class Pajaro(Animal):
    pass


class Delfin(Animal):
    pass


print(Pajaro.__bases__)
print(Animal.__subclasses__())
print('---------')
Piolin = Pajaro(2, 'amarillo')
Piolin.nacer()

Willy = Delfin(4, 'azul')
Willy.nacer()
print('---------')
print(f' Piolin es un pajaro de {Piolin.edad} años de color {Piolin.color}')
