""" Atributos de las clases """
""" Atributos de clase, de instancia """


class Pajaro:
    """ Metodo constructor que asignara atributos a nuestros pajaros """
    def __init__(self, color, especie):
        """ Self es la instancia del objeto que se va a crear para cada pajaro"""
        self.color = color
        self.especie = especie
        """ 'self.color' es el atributo, y 'color' es el parametro"""
        """ Algo similar a lo que pasa en diccionarios """

# Ejemplo de lo que esta ocurriendo mas o menos


class Autos:
    def __init__(self, mi_parametro):
        self.mi_atributo = mi_parametro


pinguino = Pajaro('Negro', 'Pinguino')
palabra = 'azul'

print(pinguino.especie)
print(pinguino.color)
print('-----------')

""" Estos son atributos de instancias por que cada 'Pajaro' puede tener diferentes caracteristicas """
""" Por ej, ahorita pinguino es nego, pero podría ser tucan y que sea color verde """
Tucan = Pajaro('Verde', 'Tucan')
print(Tucan.especie)
print(Tucan.color)
