import cv2
import face_recognition as fr

"""En este ejercicio vamos a poner el texto que obtenemos al hacer la comparación, en una de las imágenes"""

# Cargar las imagenes (primer paso)
foto_control = fr.load_image_file('Foto_Tony1.jpg')
"""Dado que el código ya está armado, si queremos comparar cualquier rostro con el mío (foto control) solo cambiamos en 
foto prueba, la imagen a utilizar"""
foto_prueba = fr.load_image_file('Foto_Channing.jpg')

# Pasar las imágenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar la cara control
lugar_cara_Tony1 = fr.face_locations(foto_control)[0]
cara_codificada_Tony1 = fr.face_encodings(foto_control)[0]

# Mostrar rectángulo en cara control
cv2.rectangle(foto_control,
              (lugar_cara_Tony1[3], lugar_cara_Tony1[0]),
              (lugar_cara_Tony1[1], lugar_cara_Tony1[2]),
              (0, 255, 0),
              2)

# Localizar la cara prueba (foto a comparar)
lugar_cara_Tony2 = fr.face_locations(foto_prueba)[0]
cara_codificada_Tony2 = fr.face_encodings(foto_prueba)[0]

# Mostrar rectángulo en cara prueba
cv2.rectangle(foto_prueba,
              (lugar_cara_Tony2[3], lugar_cara_Tony2[0]),
              (lugar_cara_Tony2[1], lugar_cara_Tony2[2]),
              (0, 255, 0),
              2)

# Sección del código para realizar la comparación
resultado = fr.compare_faces([cara_codificada_Tony1], cara_codificada_Tony2)

# Medida de la distancia
distancia = fr.face_distance([cara_codificada_Tony1], cara_codificada_Tony2)

# Mostrar resultado
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255, 0, 0),
            2)

# Mostrar las imágenes
cv2.imshow('Foto control', foto_control)
cv2.imshow('Foto prueba', foto_prueba)

# Mantener el programa abierto
cv2.waitKey(0)
