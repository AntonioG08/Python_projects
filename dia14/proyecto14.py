import cv2
import face_recognition as fr
import os
import numpy
from _datetime import datetime

"""En este proyecto haremos una base de datos para ver si los empleados de una empresa ya registraron asistencia en 
el día o si aun no lo hacen"""

# Crear base de datos
ruta = 'Empleados'
base_imagenes = []
nombres_empleados = []
"""Con este método podemos crear la lista recorriendo todos los elementos en el directorio 'Empleados' """
lista_empleados = os.listdir(ruta)

for e in lista_empleados:
    """El método 'imread' permite leer la imagen, solo debemos de pasarle el parámetro o la ruta que seguir"""
    imagen_actual = cv2.imread(f'{ruta}/{e}')
    base_imagenes.append(imagen_actual)
    """Ponemos esta configuración de append, para que el nombre no se guarde con la extensión del tipo de archivo
    que en este caso es el 'jpg' """
    nombres_empleados.append(os.path.splitext(e)[0])


# Codificar imagenes
def codificar_imagenes(imagenes):

    # Crear una lista nueva codificada
    lista_codificada = []

    # Pasar imágenes a RGB
    for i in imagenes:
        """Vamos a hacer que cada imagen de la lista de imágenes (parametro que vamos a pasarle) sea pasada a RGB con 
        el método de la librería cv2"""
        i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)

        # Codificar
        codificado = fr.face_encodings(i)[0]

        # Agregar lo codificado a la lista
        lista_codificada.append(codificado)

    # Devolver la lista codificada
    return lista_codificada


# Función para registrar los ingresos
def registrar_ingresos(persona):
    """El formato 'r+' nos permitirá además de abrir el archivo, escribirlo y editarlo"""
    f = open('Registro.csv', 'r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    """La lógica aqui es que si la persona no esta aún en la lista, es por que no ha tomado asistencia hoy y entonces
    lo guardamos en la lista. Si la persona ya está es por que ya se registró y no lo guardaremos dos veces en el 
    mismo día."""
    if persona not in nombres_registro:
        ahora = datetime.now()
        """Este método nos permitirá extraer la hora, los minutos y los segundos del string"""
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')


"""Esta variable es muy importante pues es la que tiene almacenadas todas las imágenes codificadas y listas para 
ser usadas"""
lista_empleados_codificada = codificar_imagenes(base_imagenes)

"""Con esta línea de código le pedimos al ordenador que capture una imágen usando la cámara que tenga en el momento"""
# Tomar una imagen de cámara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Leer imagen de la cámara
exito, imagen = captura.read()

if not exito:
    print('No se ha podido tomar la captura')
else:
    # Reconocer una cara en la captura
    cara_captura = fr.face_locations(imagen)

    # Codificar la cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # Buscar coincidencias
    for caracod, caraubi in zip(cara_captura_codificada, cara_captura):
        """En este método, la comparación exige como argumento, una lista, y nosotros le enviamos una lista de todos 
        los empleados actuales. Por ello es que a pesar de que en el 'for' solo sera un elemento, el programa hará
        6 comparaciones en total gracias al método, dando como resultado una lista comparada"""
        coincidencia = fr.compare_faces(lista_empleados_codificada, caracod)
        distancias = fr.face_distance(lista_empleados_codificada, caracod)

        indice_coincidencia = numpy.argmin(distancias)

        # Mostrar coincidencia si es que hay
        if distancias[indice_coincidencia] > 0.6:
            print('No hay coincidencia con ningún empleado actual')
        else:
            # Buscar el nombre del empleado coincidente
            nombre = nombres_empleados[indice_coincidencia]

            # Mostrar un rectángulo en la cara de la foto
            """Las variables van siendo almacenadas en orden. El cuadro al momento de generarse por 'facelocation'
            inicia en la esquina superior izquierda, en 'Y1', y después sigue a la derecha al límite en 'X2', luego 
            baja al límite en 'Y2' y por último sigue a la izquierda al inicio horizontal en 'X1'."""
            y1, x2, y2, x1 = caraubi
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            registrar_ingresos(nombre)

            # Mostrar la imagen obtenida
            cv2.imshow('Imagen web', imagen)

            # Mantener ventana abierta
            cv2.waitKey(0)
