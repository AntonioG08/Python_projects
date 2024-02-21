import cv2
import face_recognition as fr
import pybind11

"""En esta unidad estaremos aprendiendo a programar un software de reconocimiento facial. Para que el reconocimiento
 facial sea posible, básicamente se siguen los siguientes pasos:

 1- Reconocimiento facial
 2- Análisis facial
 3- Convertir la imagen del rostro en datos3
 4- Buscar coincidencias con una base de datos previa (fotos previas de rostros)

 Vamos a descargar visual studio community teniendo cuidado DE AGREGAR el complemento DESARROLLO ESCRITORIO C++"""
# Primero vamos a cargar las imagenes
foto_control = fr.load_image_file('Foto_Tony1.jpg')
foto_prueba = fr.load_image_file('Foto_Tony2.jpg')

"""Vamos a cambiar la forma en como python está viendo/interpretando las imágenes, pues python lo hace usando el
código RGB, por lo cual debemos hacer una modificación inicial a las imagenes"""

"""Primero usaremos la librería cv2 para lograr esto, la cual nos pide básicamente 2 parámetros, primero es la fuente o 
source 'src' y después la instrucción de que quiere que hagamos, veamos el siguiente ejemplo"""
# Pasar las imágenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

"""Ahorita veremos como ejemplo como lucen las imágenes, no es necesario siempre realizar el paso en donde se muestran
las fotos """
# Mostrar las imágenes
cv2.imshow('Foto control', foto_control)
cv2.imshow('Foto prueba', foto_prueba)

"""Dado que python muestra las imágenes y finaliza el código, usaremos un método de la librería cv2 que nos permite
mantener el código abierto hasta que alguna tecla sea pulsada"""
# Mantener el programa abierto
cv2.waitKey(0)
