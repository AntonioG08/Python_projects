import bs4
import requests
"""Vamos a obtener el texto de una parte especifica de la página web"""

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

var_sp = bs4.BeautifulSoup(resultado.text, 'lxml')

"encabezado = var_sp.select('.widget-content')"
'''Con esto nosotros buscamos dentro del link elegido, la información que contenga las clases llamadas 
overflowable-item, que en este caso son 3, la que contiene a cursos, youtube e instagram. Sin embargo, dentro de la 
 clase vienen muchos elementos, y a nosotros nos interesa el elemento "a", que significa anchor, por que justamente
 estas palabras tienen ancladas un hipervínculo para llevarnos a otro lugar'''
encabezado = var_sp.select('.overflowable-item a')
"""Este contenido que guardamos en la variable encabezado se almacena en forma de tupla, por lo cual pudieramos dejarlo
asi y solo pedirle que imprima posiciones especificas como 0, 1 o 2, o pedir en un loop que imprima cada una de ellas"""
for a in encabezado:
    print(a.getText())
"""Por último, la información en la tupla sigue tiendo informacion adicional, como la etiqueta del elemento, el 
hipervinculo que tiene anclado, etc. Por ello al final le pedimos con el método getText() que solo imprima el 
texto de estas partes"""

"print(encabezado)"
