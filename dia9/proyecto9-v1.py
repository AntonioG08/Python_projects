import shutil
""" Primera parte del proyecto 9 para descomprimir las instrucciones """


destino2 = 'C:\\Users\\togor\\Documents\\Certificados\\Python total\\Proyecto_dia9'
destino = 'C:\\Users\\togor\\Documents\\Certificados\\Python total\\Python\\dia9\\Proyecto dia9'

""" En este caso, es necesario tener el archivo zip en la misma carpeta del código python, 
en destino2 puse la ruta en donde deseo que se guarde el contenido una vez que se descomprime """
shutil.unpack_archive('Proyecto+Dia+9.zip', destino2, 'zip')

# Este código ya se ejecutó una vez, la carpeta compimida en el archivo zip ya se descomprimio (ver la ruta de "origen"
# El segundo parametro, está mal, el segundo parametro no es el origen, es el destino a donde se enviara el contenido
# que estaba comprimido en el zip.
