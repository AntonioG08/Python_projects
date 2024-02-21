""" Están también los atributos de clase """
""" Estos atributos los tienen todos los que pertenezcan a dicha clase """


class Pajaro:
    alas = 'Todas las aves tienen alas'
    alas2 = True
    """ Metodo constructor que asignara atributos a nuestros pajaros """
    def __init__(self, color, especie):
        """ Self es la instancia del objeto que se va a crear para cada pajaro"""
        self.color = color
        self.especie = especie
        """ 'self.color' es el atributo, y 'color' es el parametro"""
        """ Algo similar a lo que pasa en diccionarios """


Tucan = Pajaro('Verde', 'Tucan')
print(Tucan.especie)
print(Tucan.color)
print('---------')
""" Todos los que pertenezcan a las clases pajaros tienen alas """
""" Estos son atributos de clase, por que no dependen de la instancia, si no de la categoria"""
print(f'Esto es {Pajaro.alas2}, {Pajaro.alas}')
print('----------')


class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad


harry_potter = Personaje('Humano', True, 17)
print(f'El persona Harry potter es {Personaje.real}, el es un {harry_potter.especie}, y tiene {harry_potter.edad}')