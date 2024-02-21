""" Ejercicios sobre métodos especiales """
""" Ya hemos visto ejemplos de estos como __init__, __mro__, 
__bases__ y __subclass__ por dar algunos ejemplos """


class CD:
    def __init__(self, autor, album, canciones):
        self.autor = autor
        self.album = album
        self.canciones = canciones

    def __str__(self):
        return f'El albúm {self.album} es de {self.autor}'

    def __len__(self):
        return self.canciones

    """ Con esto ademas de hacer la función de borrar algo podemos imprimir algún mensaje al realizar 
    la acción """
    def __del__(self):
        print('se ha eliminado mi_cd')


""" Normalmente es un string, pero diferente con el tipo '__main' pero con la funcion __str__ 
podemos indicar como se debe comportar el str cuando sea solicitado o invocado """
mi_cd = CD('daddy yankee', 'Daddy Yankee Mundial', 12)
print(mi_cd)
print('--------')

""" Lo mismo podemos hacer con el largo, actualmente no nos arroja un valor de vuelta que sea coherente 
pero con la función __len__ podemos modificarlo por ejemplo: """
print(f' el album tiene {len(mi_cd)} canciones')

""" Con esta función podemos borrar instancias y dejan de existir """
del mi_cd
