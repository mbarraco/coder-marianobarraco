import time

# Ejercicio 1: encapsular el siguiente código en una función
#               y utilizarla para dibujar el tablero 10 veces

"""
FILAS = 8
COLUMNAS = 10

tablero = []
for i in range(FILAS):
    # fila = []
    # for j in range(COLUMNAS):
    #     fila.append(".")
    fila = ["."] * COLUMNAS  # listas de <COLUMNAS> elementos
    tablero.append(fila)

# tablero tienen <FILAS> elementos
for xx in tablero:
    print("  ".join(xx)) # convertir la lista en str juntada por espacios e imprimirla
"""

# def dibujar_tablero():
#     FILAS = 8
#     COLUMNAS = 10

#     tablero = []
#     for i in range(FILAS):
#         fila = ["."] * COLUMNAS
#         tablero.append(fila)

#     for xx in tablero:
#         print("  ".join(xx))

# for i in range(10):
#     dibujar_tablero()
#     print()

# Ejercicio 2: modificar la función anterior para que dibuje un "0" en
#              la 4ta fila y 5ta columna, es decir en la posición (3, 4)
# def dibujar_tablero():
#     FILAS = 8
#     COLUMNAS = 10

#     tablero = []
#     for i in range(FILAS):
#         fila = ["."] * COLUMNAS
#         tablero.append(fila)

#     tablero[3][4] = "0" # UNICA MODIFICACION

#     for xx in tablero:
#         print("  ".join(xx))

# for i in range(10):
#     dibujar_tablero()
#     print()


# Ejercicio 3: modificar la función anterior para reciba 2 parámetros que indiquen
#              en qué fila y columna dibujar el "0"


def dibujar_tablero(posicion_fila, posicion_columna):
    FILAS = 8
    COLUMNAS = 10

    tablero = []
    for i in range(FILAS):
        fila = ["."] * COLUMNAS
        tablero.append(fila)

    tablero[posicion_fila][posicion_columna] = "0"  # UNICA MODIFICACION

    for xx in tablero:
        print("  ".join(xx))


for i in range(10):
    time.sleep(1)
    dibujar_tablero(i, i)
    print()
