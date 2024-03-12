ruta_del_archivo = "archivo.txt"


f = open(ruta_del_archivo, "r")
contenido = f.readline()
print(contenido)
f.close()
print()


f = open(ruta_del_archivo, "r")
f.seek(5)
contenido = f.readline()
print(contenido)
f.close()
print()

