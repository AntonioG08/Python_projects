import bs4
import requests

# URL de base para ir cambiando el numero de paginas
url_paginas = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista con los títulos que tengan entre 4 o 5 estrellas
libros_puntuaje_alto = []

# Loop para ir buscando y pasando de pagina
for n in range(1, 51):
    url_actual = url_paginas.format(n)
    # Crear una impresion del contenido en cada pagina que vayamos pasando
    resultado = requests.get(url_actual)
    var_sp = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Obtener solo los datos de la clase del tipo product pod
    opciones = var_sp.select('.product_pod')
    for libro in opciones:
        """Debemos revisar que cumpla nuestra condicion de tener 4 o 5 estrellas"""
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            titulo = libro.select('a')[1]['title']

            # Por último queda agregar el título almacenado a nuestra lista de libros
            libros_puntuaje_alto.append(titulo)

# Parte del código para imprimir los títulos almacenados en nuestra lista
for i in libros_puntuaje_alto:
    print(i)
