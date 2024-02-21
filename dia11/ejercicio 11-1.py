import bs4
import requests

# Primer código de scrapping para obtener el encabezado de una página web

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')

print(type(resultado))
print('---------')
"""Este print es del primer scrapping donde obtenemos el código de html directo sin procesar"""
'print(resultado.text)'

# Tenemos que hacer el parcing del codigo que viene al jalarlo de la página web
""""Parsing" significa analizar y convertir un programa en un formato interno que un 
entorno de ejecución pueda realmente ejecutar, por ejemplo el motor JavaScript dentro de los navegadores"""
var_sp = bs4.BeautifulSoup(resultado.text, 'lxml')
'Este print nos va a imprimir el código html pero ya más directo y procesado print(var_sp)'
print(var_sp.select('title')[0])
print('---------------')

# Para imprimir el título solamente como texto sin etqietas hacemos lo siguiente
print(f'El título de esta página web es: {var_sp.select("title")[0].getText()}')
print('---------------')
# Plus adicional para imprimir en pantalla el número de parrafos, podemos hacer lo mismo para todas las etiquetas
print(f'El número de párrafos de la página web es de: {len(var_sp.select("p"))}')
