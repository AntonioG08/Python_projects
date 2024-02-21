from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

"""En esta unidad usaremos la libreria tkinter para crear una interfaz de un restaurante
Ya está todo listo, ahora solo queda agregar la función al botón guardar y 'resetear' """

operador = ''

"""Variables para los precios de los alimentos y bebidas"""
precio_comida = [89, 100, 240, 50, 70]
precio_bebida = [15, 18, 25, 17, 30]
precio_postre = [30, 40, 45, 60, 25]


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


def revisar_check():
    """Necesitamos un contador que vaya revisando a todos los cuadros que están checados en nuestra ventana"""
    x = 0
    for c in recuadros_comida:
        """Iniciaremos con un condicional, que depende si el cuadro esta o no seleccionado. Cuando no está seleccionado
        vale 0, y cuando lo está vale 1"""
        if variables_comida[x].get() == 1:
            """Una vez que el cuadro fue seleccionado, el estado de este es normal y ya podemos escribir en el"""
            recuadros_comida[x].config(state=NORMAL)
            """También en automático cuando se selecciona se borra el 0 que teniamos ahi por default"""
            if recuadros_comida[x].get() == '0':
                recuadros_comida[x].delete(0, END)
                """El método focus nos permite que el cursor aparezca parpadeando"""
                recuadros_comida[x].focus()
        else:
            """Esta línea de código nos regresa a el estado normal antes de seleccionar la casilla"""
            recuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    y = 0
    for b in recuadros_bebida:
        if variables_bebida[y].get() == 1:
            recuadros_bebida[y].config(state=NORMAL)
            if recuadros_bebida[y].get() == '0':
                recuadros_bebida[y].delete(0, END)
                recuadros_bebida[y].focus()
        else:
            recuadros_bebida[y].config(state=DISABLED)
            texto_bebida[y].set('0')
        y += 1

    z = 0
    for p in recuadros_postre:
        if variables_postre[z].get() == 1:
            recuadros_postre[z].config(state=NORMAL)
            if recuadros_postre[z].get() == '0':
                recuadros_postre[z].delete(0, END)
                recuadros_postre[z].focus()
        else:
            recuadros_postre[z].config(state=DISABLED)
            texto_postre[z].set('0')
        z += 1


def total():
    """Función total para calcular cuando hemos metido las cantidades"""
    subtotal_comida = 0
    p = 0
    for cantidad in texto_comida:
        subtotal_comida = subtotal_comida + (float(cantidad.get()) * precio_comida[p])
        p += 1

    subtotal_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        subtotal_bebida = subtotal_bebida + (float(cantidad.get()) * precio_bebida[p])
        p += 1

    subtotal_postre = 0
    p = 0
    for cantidad in texto_postre:
        subtotal_postre = subtotal_postre + (float(cantidad.get()) * precio_postre[p])
        p += 1

    sub_total = subtotal_comida + subtotal_bebida + subtotal_postre
    impuestos = sub_total * 0.12
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(subtotal_comida, 2)}')
    var_costo_bebida.set(f'$ {round(subtotal_bebida, 2)}')
    var_costo_postre.set(f'$ {round(subtotal_postre, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuesto.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    """Ponemos esta línea para asegurarnos de borrar lo que pudiera haber y el recibo inicie en blanco"""
    texto_recibo.delete(1.0, END)
    num_recibo = f'No. recibo - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    """esta variable contiene una fecha mucho más normal a lo usado cotidianamente"""
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    """Parte del código donde empezamos a configurar el encabezado de la parte del recibo"""
    texto_recibo.insert(END, f'\t\tDatos\n {num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 52 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tPrecio items\n')
    texto_recibo.insert(END, f'-' * 63 + '\n')

    """Ciclos para meter en el recibo todos los alimentos seleccionados con sus cantidades"""
    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comida[x]}\t\t{comida.get()}\t'
                                     f'$ {int(comida.get()) * precio_comida[x]}\n')
        x += 1

    y = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebida[y]}\t\t{bebida.get()}\t'
                                     f'$ {int(bebida.get()) * precio_bebida[y]}\n')
        y += 1

    z = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postre[z]}\t\t{postre.get()}\t'
                                     f'$ {int(postre.get()) * precio_postre[z]}\n')
        z += 1

    """Bloque de código para agregar los costos de los alimentos en el recibo"""
    texto_recibo.insert(END, f'-' * 63 + '\n')
    texto_recibo.insert(END, f'Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de los postres: \t\t\t{var_costo_postre.get()}\n')

    """Bloque de código para agregar el subtotal, IVA y total en el recibo"""
    texto_recibo.insert(END, f'-' * 63 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Imputestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')

    texto_recibo.insert(END, f'*' * 52 + '\n')
    texto_recibo.insert(END, f'Gracias por su preferencia, vuelva pronto')


def guardar():
    """Estamos guardando en una variable el texto que metimos en la variable 'texto_recibo' y usamos el método get
    para pedirle que obtenga de principio a fin el contenido"""
    info_recibo = texto_recibo.get(1.0, END)
    """Con la configuración a continuación en modo ponemos write='w' y en extension '.txt' que es las notas"""
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    """Ponemos que se despliegue un mensaje de texto que le notifica al usuario que se guardo el recibo, para esto 
    ponemos un encabezado primero y después el cuerpo del mensaje"""
    messagebox.showinfo('Información', 'Su recibo ha sido guardado con éxito')


def resetear():
    """Esta línea elimina el contenido de la parte del recibo"""
    texto_recibo.delete(0.1, END)

    """Estos ciclos hacen que las casillas vuelvan a un valor inicial '0' """
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    """Estos ciclos hacen que los cuadros también se desactiven además de volver a un valor inicial de '0' """
    for cuadro in recuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in recuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in recuadros_postre:
        cuadro.config(state=DISABLED)

    """Con estos ciclos también logramos que se quite la casilla de verificación de los checkbuttons"""
    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


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
                         variable=variables_comida[contador],
                         command=revisar_check)
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
    """El state=DISABLED hace que no podamos modificar el texto o escribir dentro del recuadro. En la funcion
    'revisar_check' este cambia a 'NORMAL' y ya nos permite editarlo"""
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
                         variable=variables_bebida[contador],
                         command=revisar_check)
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
                         variable=variables_postre[contador],
                         command=revisar_check)
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

# Sección del código para elaborar los BOTONES
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 13, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=7)

    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

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
