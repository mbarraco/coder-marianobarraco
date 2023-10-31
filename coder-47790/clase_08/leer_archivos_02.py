from time import sleep

mi_archivo = open("mi_archivo_de_texto.txt", "r")


print(mi_archivo.read())

mi_archivo.seek(0)

for linea in mi_archivo.readlines():
    linea_editada = linea.title().replace("e", "3")
    print(linea_editada)
    sleep(0.5)

mi_archivo.seek()

print(mi_archivo.readline())
print(mi_archivo.readline())


mi_archivo.close()
