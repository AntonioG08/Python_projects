import cv2
import face_recognition as fr

"""En este tercer ejercicio vamos a almacenar los rostros ya reconocidos y pedirle al software que nos haga una 
comparativa con otros rostros"""

# Primero vamos a cargar las imagenes
foto_control = fr.load_image_file('Foto_Tony1.jpg')
"""Dado que el código ya está armado, si queremos comparar cualquier rostro con el mío (foto control) solo cambiamos en 
foto prueba, la imagen a utilizar"""
foto_prueba = fr.load_image_file('Foto_Channing.jpg')

# Pasar las imágenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

"""Con esta sección de código le estamos pidiendo al programa que identifique en el espacio, cual es el lugar donde 
está el rostro, y que además lo codifique para que la computadora pueda interpretarlo a nivel de código-números"""
# Localizar la cara control
lugar_cara_Tony1 = fr.face_locations(foto_control)[0]
"""El lugar de la cara será delimitada en un rectángulo, ej. (139, 454, 268, 325) que en orden, sería primero el 
límite superior, luego el límite derecho, luego el límite inferior y por último el límite izquierdo, formando así 4 
líneas que delimitan el área de la cara"""
cara_codificada_Tony1 = fr.face_encodings(foto_control)[0]

# Mostrar rectángulo en cara control
cv2.rectangle(foto_control,
              (lugar_cara_Tony1[3], lugar_cara_Tony1[0]),
              (lugar_cara_Tony1[1], lugar_cara_Tony1[2]),
              (0, 255, 0),
              2)

# Localizar la cara prueba
lugar_cara_Tony2 = fr.face_locations(foto_prueba)[0]
cara_codificada_Tony2 = fr.face_encodings(foto_prueba)[0]

# Mostrar rectángulo en cara prueba
cv2.rectangle(foto_prueba,
              (lugar_cara_Tony2[3], lugar_cara_Tony2[0]),
              (lugar_cara_Tony2[1], lugar_cara_Tony2[2]),
              (0, 255, 0),
              2)

# Sección del código para realizar la comparación
"""Este método pide que ingresemos una lista, sin embargo ahorita solo tenemos una imagen, no una lista con muchas 
imágenes. Es por ello que pasaremos el argumento en tipo de lista, aun que sea técnicamente una lista de solo 1 objeto"""
resultado = fr.compare_faces([cara_codificada_Tony1], cara_codificada_Tony2)
print(resultado)

# Mostrar las imágenes
cv2.imshow('Foto control', foto_control)
cv2.imshow('Foto prueba', foto_prueba)

# Mantener el programa abierto
cv2.waitKey(0)
