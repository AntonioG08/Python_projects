import cv2
import face_recognition as fr

"""En este cuarto ejercicio ahora veremos la medida interna que usa FR para estimar la diferencia entre el rostro
de una persona y otra. Esta 'distancia' es de 0.6 por default, y si resulta ser mayor a esta, entonces el programa 
interpreta que no hay coincidencia en ambos rostros"""

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
"""El último valor es la tolerancia, que inicialmente está en 0.6, pero puede ser modificada para ser mayor o menor"""
resultado = fr.compare_faces([cara_codificada_Tony1], cara_codificada_Tony2)
"resultado = fr.compare_faces([cara_codificada_Tony1], cara_codificada_Tony2, 0.3)"
print(resultado)

# Mostrar las imágenes
cv2.imshow('Foto control', foto_control)
cv2.imshow('Foto prueba', foto_prueba)

# Medida de la distancia
distancia = fr.face_distance([cara_codificada_Tony1], cara_codificada_Tony2)
print(distancia)

# Mantener el programa abierto
cv2.waitKey(0)