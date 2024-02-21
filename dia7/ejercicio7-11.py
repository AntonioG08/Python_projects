""" Ejercicios ahora sobre el polimorfismo """


class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice muu')


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beee')


vaca1 = Vaca('Aurora')
oveja1 = Oveja('Dolly')
"""
vaca1.hablar()
oveja1.hablar() """

animales = [vaca1, oveja1]
for animal in animales:
    animal.hablar()
print('---------')


def animal_hablar(animal2):
    animal2.hablar()


animal_hablar(vaca1)