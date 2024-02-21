import bs4
import requests
"""Vamos a aprovechar una pagina web para hacer scrapping y probar esto en obtener los títulos de una tienda
ficticia de libros"""

'''Pagina ficticia: https://toscrape.com/'''
"""Link de las paginas de la tienda de libros, solo cambia eñ numerador 2,3,4 etc etc"""
url_paginas = 'https://books.toscrape.com/catalogue/page-{}.html'

"""for n in range(1, 11):
    print(url_paginas.format(n))
Con esta linea de codigo de arriba ´podría crear todos los links de las listas de la pagina"""
resultado = requests.get(url_paginas.format('1'))
var_sp = bs4.BeautifulSoup(resultado.text, 'lxml')

libros = var_sp.select('.product_pod')
"""Cuando haya en HTML espacios en blanco, en el código debemos escribir un punto '.' para indicar que ahi hay 
un espacio en blanco"""
ejemplo1 = libros[0].select('.star-rating.Three')
"""Podemos ver esta tupla como un diccionario y pedirle que imprima justo la informacion contenida en el titulo"""
ejemplo2 = libros[0].select('a')[1]['title']

print(ejemplo2)
