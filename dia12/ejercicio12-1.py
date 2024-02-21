from tkinter import *
"""En esta unidad usaremos la libreria tkinter para crear una interfaz de un restaurante
Primero en este ejercicio veremos como hacer la configuración básica de nuestra pestaña"""

# Primero debemos de inicializar tkinter como si se tratara de una función, y ya después podemos usar sus metodos
programa = Tk()

# Parte del código para configurar el tamaño de nuestra pestaña
"""Aqui vamos a hacer la configuración de la pestaña, primero son los pixeles de alto por el ancho, y después 
es la posición en la cual aparecera la pestaña. El orígen es la esquina superior izquierda, por lo cual a partir de 
ahí podemos desplazar la ubicación en que aparcerá"""
programa.geometry('1020x630+0+0')

# Parte del código que evita que el usuario ajuste la pestaña
"""Por el momento la pestaña no esta planeada para ser ajustable en el tamaño, por ello bloquearemos esta opció 
al usuario del programa, para ello pondremos el atributo 'False' en el eje X y el eje Y"""
programa.resizable(False, False)

# Parte del código donde modificamos el título de la ventana efrfrf
programa.title('Gonzalitos - Sistema de facturación')

# Parte del código para modificar el color de fondo de nuestra pestaña
"https://www.plus2net.com/python/tkinter-colors.php"
"Podemos usar un nombre directo, arriba esta el directorio, o usar el cógido RGB"
programa.config(bg='cadetblue3')

# Parte del código que evita que la pestaña se cierre
programa.mainloop()
