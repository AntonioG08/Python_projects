from tkinter import *
"""En esta unidad usaremos la libreria tkinter para crear una interfaz de un restaurante
En este segundo ejercicio dividiremos en secciones la pestaña hecha"""

# Primero debemos de inicializar tkinter como si se tratara de una función, y ya después podemos usar sus metodos
programa = Tk()

# Parte del código para configurar el tamaño de nuestra pestaña
"""Configuración del alto, ancho y orígen de la pestaña"""
programa.geometry('1020x630+0+0')

# Parte del código que evita que el usuario ajuste la pestaña
"""Bloqueamos el ajuste de la pestaña poniendo False en los ejes X y Y"""
programa.resizable(False, False)

# Parte del código donde modificamos el título de la ventana
programa.title('Gonzalitos - Sistema de facturación')

# Parte del código para modificar el color de fondo de nuestra pestaña
"https://www.plus2net.com/python/tkinter-colors.php"
"Podemos usar un nombre directo, arriba esta el directorio, o usar el cógido RGB"
programa.config(bg='cadetblue3')

# Panel Superior
"""En esta configuración 'bd' es borde, 'relief' es el relieve el cual tiene 5 posibles opciones, en el cuadro de 
información de 'Frame' podemos ver las 5 opciones"""
panel_superior = Frame(programa, bd=5, relief=RAISED)
"""Con esto aseguramos que el panel este en la parte superior, al elegir en 'side' la opcion 'TOP', sin embargo, con
esto el panel aun no se verá pues no tiene contenido ni hemos elegido su tamaño y otras opciones"""
panel_superior.pack(side=TOP)

# Etiqueta Panel Superior
"""Aqui elegimos varios atributos a configurar como el ancho, el 'foreground' que es el color de texto, el 'font' que
es el estilo del texto y su tamaño, y 'background' que es el color de fondo del panel"""
etiqueta_titulo = Label(panel_superior, width=22, text='Sistema de Facturación', fg='azure3', font=('Dosis', 58),
                        bg='cornsilk2')
"""Aqui elegimos el espacio en fila y columna en donde será desplegada la etiqueta del panel superior"""
etiqueta_titulo.grid(row=0, column=0)

# Panel Izquierda
panel_izq = Frame(programa, bd=5, relief=RAISED)
panel_izq.pack(side=LEFT)

# Panel Costos
panel_costos = Frame(panel_izq, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# Panel Comidas
panel_comidas = LabelFrame(panel_izq, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure3')
panel_comidas.pack(side=LEFT)

# Panel Bebidas
panel_bebidas = LabelFrame(panel_izq, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure3')
panel_bebidas.pack(side=LEFT)

# Panel Postres
panel_postres = LabelFrame(panel_izq, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure3')
panel_postres.pack(side=LEFT)

# Panel Derecha
panel_der = Frame(programa, bd=5, relief=RAISED)
panel_der.pack(side=RIGHT)

# Panel Calculadora
panel_calculadora = Frame(panel_izq, bd=1, relief=FLAT, bg='cornsilk2')
"""Por defecto si no ponemos nada el panel estará en la parte superior"""
panel_calculadora.pack()

# Panel Recibo
panel_recibo = Frame(panel_izq, bd=1, relief=FLAT, bg='cornsilk2')
"""Por defecto si no ponemos nada el panel estará enseguida del ultimo colocado"""
panel_recibo.pack()

# Panel Botones
panel_botones = Frame(panel_izq, bd=1, relief=FLAT, bg='cornsilk2')
"""Por defecto si no ponemos nada el panel estará enseguida del ultimo colocado"""
panel_botones.pack()

# Lista de nuestros productos
lista_comida = ['Pollo', 'Pizza', 'Salmon', 'Torta', 'Baguette']
lista_bebida = ['Agua', 'Coca Cola', 'Cerveza', 'Jugo', 'Vino']
lista_postre = ['Brownie', 'Flan', 'Pastel', 'Mousse', 'Helado']

# Generador de artículos de comida
variables_comida = []
recuadros_comida = []
texto_comida: list = []
contador = 0
"""Estamos creando un checkbox con cada uno de los alimentos de las listas creadas previamente. en este caso, el 
'onvalue' y 'offvalue' es el valor que tendrá el checkbox al estar marcado o no"""
for comida in lista_comida:

    # Este bloque en el loop crea loa CheckButtons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador])
    """Las filas se van iterando, es decir, en el contador 0 ira el primer alimento, luego pasamos a la fila 2 y asi
    sucesivamente. Con sticky W nos aseguremos que este todo pegado a la izquierda con 'West' """
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # Este bloque en el loop crea los recuadros para entradas
    recuadros_comida.append('')
    texto_comida.append('')
    recuadros_comida[contador] = Entry(panel_comidas,
                                       font=('Dosis', 18, 'bold'),
                                       bd=1,
                                       width=6,
                                       state=DISABLED,
                                       textvariable=texto_comida[contador])
    recuadros_comida[contador].grid(row=contador,
                                    column=1)
    contador += 1

# Generador de artículos de bebida
variables_bebida = []
recuadros_bebida = []
texto_bebida: list = []
contador = 0
for bebida in lista_bebida:

    # Este bloque en el loop crea loa CheckButtons
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador])
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # Este bloque en el loop crea los recuadros para entradas
    recuadros_bebida.append('')
    texto_bebida.append('')
    recuadros_bebida[contador] = Entry(panel_bebidas,
                                       font=('Dosis', 18, 'bold'),
                                       bd=1,
                                       width=6,
                                       state=DISABLED,
                                       textvariable=texto_bebida[contador])
    recuadros_bebida[contador].grid(row=contador,
                                    column=1)
    contador += 1

# Generador de artículos de postre
variables_postre = []
recuadros_postre = []
texto_postre: list = []
contador = 0
for postre in lista_postre:

    # Este bloque en el loop crea loa CheckButtons
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador])
    postre.grid(row=contador,
                column=0,
                sticky=W)

    # Este bloque en el loop crea los recuadros para entradas
    recuadros_postre.append('')
    texto_postre.append('')
    recuadros_postre[contador] = Entry(panel_postres,
                                       font=('Dosis', 18, 'bold'),
                                       bd=1,
                                       width=6,
                                       state=DISABLED,
                                       textvariable=texto_postre[contador])
    recuadros_postre[contador].grid(row=contador,
                                    column=1)
    contador += 1

# Parte del código que evita que la pestaña se cierre
programa.mainloop()
