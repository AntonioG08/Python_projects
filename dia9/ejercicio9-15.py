import zipfile
import shutil
""" Ejercicios con comprimir y descomprimir archivos """

# Utilizando zip file
""" Con este código podemos crear una carpeta comprimida, y arrastrar 2 archivos existentes
dentro de la nueva carpeta """
mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')
mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')
mi_zip.close()


# Utilizando shutil
carpeta_origen = 'C:\\Users\\togor\\Documents\\Certificados\\Python total'
archivo_destino = 'Todo_comprimido'

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)
shutil.unpack_archive('Todo_comprimido.zip', 'Extracción terminada', 'zip')



