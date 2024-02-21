from collections import defaultdict
""" Importaremos ahora 'defaultdict' que sería algo como 
'diccionario por defecto' """

mi_dic = {'uno': 'rojo', 'dos': 'verde', 'tres': 'azul'}
print(mi_dic['dos'])
print('-------')

"""En caso de solicitar algo que no existe, en vez de enviarnos a error directo, nos da el mensaje 
'nada' """
mi_dic2 = defaultdict(lambda: 'nada')
mi_dic2['uno'] = 'Hola'
print(mi_dic2)
print(mi_dic2['tres'])
print(mi_dic2)
