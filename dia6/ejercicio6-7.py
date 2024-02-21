from pathlib import Path, PureWindowsPath
""" Ejercicios sobre pathlib """

carpeta = Path('C:/Users/togor/Documents/Certificados/Python total/Texto_prueba_dia6.txt')

# Ahora este es un archivo tipo 'path' y tiene diferentes acciones
print(carpeta.read_text())

print('--------')
print(carpeta.name)

print('--------')
if not carpeta.exists():
    print('Si existe')
else:
    print('no existe')

print('----------')
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)



