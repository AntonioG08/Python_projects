""" Métodos de clases """
""" Tecnicamente init es un método de clase, pero viene por default en todas """


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


piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(50)

