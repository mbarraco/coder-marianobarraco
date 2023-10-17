mi_archivo = open("mi_archivo_1697583012.220702.txt", "r")


contenido = mi_archivo.read()
print(contenido)

contenido_2 = mi_archivo.read()
print(contenido_2)

mi_archivo.seek(0)
contenido_3 = mi_archivo.read()
print(contenido_3)
