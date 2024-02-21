""" Ahora serán ejercicios sobre herencias multiples """


class Padre:
    def hablar(self):
        print('Hola mundo')


class Madre:
    def reir(self):
        print('Ja Ja Ja')

    """ Aun que madre cambie el parametro hablar, en hijo se invoco primero a padre, por ende 
    se hereda el hablar de padre"""
    def hablar(self):
        print('Holaa')


class Hijo(Padre, Madre):
    def trabajar(self):
        print('Me gusta ir a la oficina')
    pass


class Nieto(Hijo):
    pass


""" Ahora nieto tiene todos los atributos de hijo, que a su vez viene de madre y padre"""
mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
mi_nieto.trabajar()
print('---------')
print(Nieto.__mro__)

