ruta_del_archivo = "archivo.txt"

f = open(ruta_del_archivo, "r")
contenido = f.read()
f.close()
print(contenido)
print()


f = open(ruta_del_archivo, "r")
contenido = f.readline()
print(contenido)
f.close()
print()


f = open(ruta_del_archivo, "r")
contenido = f.readlines()
print(contenido)
f.close()
print()

import time
for line in contenido:
    time.sleep(1)
    print(line)