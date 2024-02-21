""" Ejercicio de métodos de clases """


class Pajaro:
    alas = 'Todas las aves tienen alas'
    alas2 = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio')

    def volar(self, metros):
        print(f'El pajaro voló {metros} metros')
        """ Agregamos la invocación a piar para mostrar que los métodos de instancia pueden
        ACCEDER a otros métodos """
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'ahora el pajaro es {self.color}')

    """ cls es clase, por ende el argumento que recibe es el de clase """
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'puso {cantidad} huevos')
        """ Marca error en la siguiente linea por  que no recibe como argumentos self, si no a la clase """
        """  print(f'el color es {self.color}')  """

        """ Esta línea si se puede por que accede al atributo de la CLASE 'alas' """
        cls.alas = False
        print(Pajaro.alas)

    """ Estos métodos no hacen referencia ni a la clase ni a la instancia """
    """ Es por ello que al abrir paréntesis no sale ni cls ni self """
    @staticmethod
    def mirar():
        """ Ninguna de las siguientes líneas serán posibles, por que en clase estática
        no podemos entrar ni a clases ni a instancias """
        """ self.color = rojo """
        """ cls. alas = True"""
        print('el pajaro mira')


""" Al ser método de clase este si se puede invocar de manera 'directa' """
Pajaro.poner_huevos(3)
""" Este otro al contrario no se hará si no tiene el 'self' """
"""  Pajaro.piar()  """
print('---------')
Pajaro.mirar()