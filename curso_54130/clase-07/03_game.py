import time


filas = 8
columnas = 8

tablero = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(".")
    tablero.append(fila)

# print(tablero)

print(f"_________________________TABLER0 1")
for xx in tablero:
    time.sleep(0.2)
    print("  ".join(xx))

# 1. En la tercer fila y séptima columna de tablero, colocar un "0"

tablero[2][6] = "0"
print(f"_________________________TABLER0 2")
for xx in tablero:
    time.sleep(0.2)
    print("  ".join(xx))
