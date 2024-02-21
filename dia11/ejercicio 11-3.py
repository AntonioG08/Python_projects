import bs4
import requests
"""Vamos a obtener una imágen específica de la página web"""

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2023/04/domina-la-regresion-lineal-paso-paso-en.html')

var_sp = bs4.BeautifulSoup(resultado.text, 'lxml')

'''imagen = var_sp.select('img')
for i in imagen:
    print(i)'''

"""Ahora vamos a probar a imprimir unicamente la imagen que nos interesa"""
imagen = var_sp.select('img')[1]['src']
print(imagen)
print('-----------')

imagen_2 = requests.get(imagen)
"print(imagen_2.content)"
'''Esta manera nos permite tener la imagen descargada, sin embargo por default nos va a aparecer como en archivo
binario, por que ese es el formato en el que la imagen está almacenada en internet y el ordenador la interpreta. Para
ello vamos a usar el siguiente código para poderla descargar y visualizar'''

f = open('Imagen_prueba.png', 'wb')
f.write(imagen_2.content)
f.close()
"""Con esta linea de codigo nosotros usamos el método de escribir para crear un archivo llamado imagen prueba, y le 
especificamos que sea 'write binary', es decir, que va a decodificar un binario. Es el mismo método usado cuando 
queriamos crear textos y que se almacenarán en el bloc de notas. Por último nunca hay que olvidar cerrarlo."""
