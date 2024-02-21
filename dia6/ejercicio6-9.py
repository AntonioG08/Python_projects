from os import system
"""Ejercicio sobre como limpiar la consola"""

nombre = input('Dime tu nombre: ').lower()
apellido = input('Dime tu apellido: ').lower()
system('cls')
print(f'tu nombre es {nombre} {apellido}')
