""" Ejemplo de uno de los ejercicios de prueba """


class Mago:
    def atacar(self):
        print("Ataque mágico")


class Arquero:
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai:
    def atacar(self):
        print("Ataque con katana")


magico = Mago()
flechas = Arquero()
Asia = Samurai()

personajes = [flechas, magico, Asia]

for ataque in personajes:
    ataque.atacar()