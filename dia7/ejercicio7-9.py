""" Recordemos que en la heredación de métodos, la clase hija puede tener
los métodos heredados, los modificados, y métodos TOTALMENTE nuevos """

""" Un hijo puede heredar cosas de su padre y su madre, una clase puede heredar de varias clases"""
""" Pero, el Hijo de el hijo, también estaría heredando todo eso """


class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('este animal ha nacido')

    def hablar(self):
        print('emite un sonido')


class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        """self.edad = edad
        self.color = color"""
        """ Es muy util esto cuando tenemos muchas lineas de variables y se heredan, para no volver a 
        escribir una por una, de lo contrario se vería como arriba """
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('pio')

    def volar(self, metros):
        print(f'el pajaro vuela {metros} metros')


Perro = Animal(2, 'rojo')
Perro.hablar()
print(f'Cliford es un perro de {Perro.edad} años color {Perro.color}')
print('---------')

""" Ahora dice pio por que se sobreescribio y modifico el valor y para pajaro es diferente"""
Piolin = Pajaro(2, 'amarillo', 38)
Piolin.hablar()
Piolin.volar(105)

