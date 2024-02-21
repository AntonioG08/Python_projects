"""Inicio de ejercicio de funciones"""

# Metodo lstrip
txt = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
x = txt.lstrip(',:_#%')
print(x)
print('--------')

# Metodo insert
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, 'naranja')
print(frutas)
print('--------')

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)
