import time


filas = 8
columnas = 8

tablero = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(".")
    tablero.append(fila)

j = 0
while j < 8:
    time.sleep(2)
    tablero[2][j] = "0"
    for xx in tablero:
        print("  ".join(xx))
    j += 1
    if j == 8:
        j = 0
    print("_____________________________________________")
