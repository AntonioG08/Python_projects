from tkinter import *

"""En esta unidad usaremos la libreria tkinter para crear una interfaz de un restaurante
En este cuarto ejercicio, la pestaña ya quedo diseñada en su totalidad. Ahora haremos que los botones funcionen
realmente"""

operador = ''


def click(numero):
    global operador
    operador = operador + numero
    """ACLARACION, la variable que almacena el contenido es 'OPERADOR', por ende si no borramos visor, se empezaría a 
    concatenar el doble de lo que queremos. Para ello primero borramos lo que tenia visor y re-escribimos el nuevo 
    contenido actualizado que está en 'operador'  """
    visor.delete(0, END)
    visor.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor.delete(0, END)


def resultado():
    global operador
    """La función 'eval' que es evaluar, leera el string y lo interpretará, es decir, si tenemos '4+5' sabrá que es 
    una suma y nos dará el resultado"""
    resultado_final = str(eval(operador))
    """El '0', 'END' significa que borrara todo lo que haya de principio a fin"""
    visor.delete(0, END)
    visor.insert(0, resultado_final)
    operador = ''


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
panel_superior = Frame(programa, bd=5, relief=RAISED)
panel_superior.pack(side=TOP)

# Etiqueta Panel Superior
"""Aqui elegimos varios atributos a configurar como el ancho, el 'foreground' que es el color de texto, el 'font' que
es el estilo del texto y su tamaño, y 'background' que es el color de fondo del panel"""
etiqueta_titulo = Label(panel_superior, width=22, text='Sistema de Facturación', fg='azure3', font=('Dosis', 58),
                        bg='cornsilk2')
"""Aqui elegimos el espacio en fila y columna en donde será desplegada la etiqueta del panel superior"""
etiqueta_titulo.grid(row=0, column=0)

# Panel Izquierda
panel_izq = Frame(programa, bd=2, relief=RAISED)
panel_izq.pack(side=LEFT)

# Panel Costos
panel_costos = Frame(panel_izq, bd=1, relief=FLAT, bg='azure4', padx=40)
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
panel_der = Frame(programa, bd=2, relief=RAISED)
panel_der.pack(side=RIGHT)

# Panel Calculadora
panel_calculadora = Frame(panel_der, bd=2, relief=FLAT, bg='cornsilk2')
"""Por defecto si no ponemos nada el panel estará en la parte superior"""
panel_calculadora.pack()

# Panel Recibo
panel_recibo = Frame(panel_der, bd=2, relief=FLAT, bg='cornsilk2')
"""Por defecto si no ponemos nada el panel estará enseguida del ultimo colocado"""
panel_recibo.pack()

# Panel Botones
panel_botones = Frame(panel_der, bd=2, relief=FLAT, bg='cornsilk2')
"""Por defecto si no ponemos nada el panel estará enseguida del ultimo colocado"""
panel_botones.pack()

'---------------------------'
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
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
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
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
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
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    recuadros_postre[contador] = Entry(panel_postres,
                                       font=('Dosis', 18, 'bold'),
                                       bd=1,
                                       width=6,
                                       state=DISABLED,
                                       textvariable=texto_postre[contador])
    recuadros_postre[contador].grid(row=contador,
                                    column=1)
    contador += 1

'----------------------------'
# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiquetas para los costos y campos de entrada
etiqueta_costos_comida = Label(panel_costos,
                               text='Costo de la comida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costos_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=30)
'--------------'
etiqueta_costos_bebida = Label(panel_costos,
                               text='Costo de la bebida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costos_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=30)
'--------------'
etiqueta_costos_postre = Label(panel_costos,
                               text='Costo del postre',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costos_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=30)

'Empieza la parte de los totales -------------------------------'
etiqueta_subtotal = Label(panel_costos,
                          text='Subtotal',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=30)
'-------------'
etiqueta_impuestos = Label(panel_costos,
                           text='impuestos',
                           font=('Dosis', 12, 'bold'),
                           bg='azure4',
                           fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_impuesto)
texto_impuestos.grid(row=1, column=3, padx=30)
'-------------'
etiqueta_total = Label(panel_costos,
                       text='total',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=30)

# Sección del código para elaborar los botones
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 13, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=7)
    boton.grid(row=0,
               column=columnas)
    columnas += 1

# Sección del código para el recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=35,
                    height=10)
texto_recibo.grid(row=0, column=0)

# Calculadora
visor = Entry(panel_calculadora,
              font=('Dosis', 16, 'bold'),
              width=28,
              bd=1)
visor.grid(row=0,
           column=0,
           columnspan=5)
"""Código para hacer los botones de la calculadora, los pusimos así por que estamos recorriendo los botones por 
filas, desde la fila que está hasta arriba en una calculadora común"""
botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', 'x', 'CE', 'B', '0', '/']
botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=6)
    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila += 1
    columna += 1
    if columna == 4:
        columna = 0

"""Usamos lambda como comando o funcion, que nos permitira incorporar el argumento que necesita la funcion"""
botones_guardados[0].config(command=lambda: click('7'))
botones_guardados[1].config(command=lambda: click('8'))
botones_guardados[2].config(command=lambda: click('9'))
botones_guardados[3].config(command=lambda: click('+'))
botones_guardados[4].config(command=lambda: click('4'))
botones_guardados[5].config(command=lambda: click('5'))
botones_guardados[6].config(command=lambda: click('6'))
botones_guardados[7].config(command=lambda: click('-'))
botones_guardados[8].config(command=lambda: click('1'))
botones_guardados[9].config(command=lambda: click('2'))
botones_guardados[10].config(command=lambda: click('3'))
botones_guardados[11].config(command=lambda: click('*'))
botones_guardados[12].config(command=resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click('0'))
botones_guardados[15].config(command=lambda: click('/'))

# Parte del código que evita que la pestaña se cierre
programa.mainloop()
