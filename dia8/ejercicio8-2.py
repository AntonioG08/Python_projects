""" El ejercicio 8-1 fue sobre los módulos y paquetes donde creamos los nuestros propios """
""" Este ejercicio ahora será sobre fallas y posibles errores en python con el manejo de errores
de los siguientes comandos """

""" Try
Except
Finally """

"""Hagamos una función que de error a propósito """


def suma():
    x = int(input('Ingrese valor para x: '))
    y = int(input('Ingrese valor para y: '))
    print(x + y)
    print('Gracias por sumar' + x)


try:
    """Código que queremos probrar"""
    suma()

except TypeError:
    """Código que se ejecutará si no hay error"""
    print('Esta intentando concatenar STR con INT')

except ValueError:
    print('Ha ingresado algo que no es un número')

else:
    print('Hiciste todo bien')

finally:
    """Código que se va a ejecturar de todos modos"""
    print('Eso fue todo')

""" Correr el código haciéndolo bien y mal para notar las diferencias"""
