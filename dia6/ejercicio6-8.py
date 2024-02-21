from pathlib import Path
""" Ejercicios con path """

base = Path.home()
guia = Path("Casa", "cuarto1")
print(base)
print('-------')
print(guia)
print('--------')
guia2 = Path(base, 'Casa', 'Cuarto1')
print(guia2)

# Este nos retorna a un nivel anterior
print('---------')
print(guia2.parent)
print('---------')
print(guia2.parent.parent)

