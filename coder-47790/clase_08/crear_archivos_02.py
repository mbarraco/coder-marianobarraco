from time import sleep, time
import random

nombre_de_archivo = f"mi_archivo_{time()}.txt"
mi_archivo = open(nombre_de_archivo, "w")

for i in range(10):
    xx = str(random.randint(0, 19))
    mi_archivo.write(xx)
    # mi_archivo.write(",")
    mi_archivo.write("\n")
