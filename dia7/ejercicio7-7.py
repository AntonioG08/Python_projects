""" Práctica 3 de métodos """


class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1
