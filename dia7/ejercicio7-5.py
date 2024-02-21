""" Lección sobre decoradores """
""" Están los métodos de clase, métodos de instancia, métodos estáticos """
""" métodos de instancia son los normales """
""" métodos de clase son @classmethod """
""" métodos estáticos son @staticmethod """


class Pajaro:
    alas = 'Todas las aves tienen alas'
    alas2 = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'Pio, mi color es {self.color}')
        print('Pio, mi especie es {}'.format(self.especie))
        """ Dos maneras distintas de invocar el atributo de instancia"""

    def volar(self, metros):
        print(f'El pajaro voló {metros} metros')
        """ Agregamos la invocación a piar para mostrar que los métodos de instancia pueden
        ACCEDER a otros métodos """
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'ahora el pajaro es {self.color}')


piolin = Pajaro('amarillo', 'canario')
print(piolin.color)
print('-----------')
piolin.pintar_negro()
print(piolin.color)
""" Este es un método de instancia, y como podemos ver pueden acceder y
 MODIFICAR los atributos de instancia, ej. ahora el color es negro y no amarillo """
print('-----------')
piolin.volar(40)
print('----------')
""" Con esto también podemos modificar el estado de la clase"""
piolin.alas = False
print(f'ahora es {piolin.alas} que piolin tiene alas')