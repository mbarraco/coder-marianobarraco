import time

# Ejercicio 1: explicar:
#               a) lo que hace este código y qué se verá por la consola.
#               b) cuántas veces lo hace y si tendrá algún error


# Ejercicio 2: solucionar los errores si los hubiera, si no, pasar al siguiente ejercicio.

"""
FILAS = 20
COLUMNAS = 50

def dibujar_tablero(posicion_fila, posicion_columna):
    tablero = []
    for i in range(FILAS):
        fila = ["."] * COLUMNAS
        tablero.append(fila)

    tablero[posicion_fila][posicion_columna] = "0" # UNICA MODIFICACION
    for xx in tablero:
        print("  ".join(xx))


posicion_fila = 0
posicion_columna = 0
while True:
    posicion_fila += 1
    posicion_columna += 1
    if posicion_fila > FILAS - 1:
        posicion_fila = 0
    if posicion_columna > COLUMNAS - 1:
        posicion_columna = 0

    dibujar_tablero(posicion_fila, posicion_columna)
    print()
    time.sleep(0.5)
"""

# Ejercicio 3: "encapsular" las líneas de código de "posicionamiento" en una función que se llame "mover"


"""

FILAS = 6
COLUMNAS = 8
def dibujar_tablero(posicion_fila, posicion_columna):
    tablero = []
    for i in range(FILAS):
        fila = ["."] * COLUMNAS
        tablero.append(fila)

    tablero[posicion_fila][posicion_columna] = "0" # UNICA MODIFICACION
    for xx in tablero:
        print("  ".join(xx))


def mover(fila, columna):
    fila += 1
    columna += 1
    if fila > FILAS - 1:
        fila = 0
    if columna > COLUMNAS - 1:
        columna = 0

    return fila, columna


posicion_fila = 0
posicion_columna = 0
while True:
    dibujar_tablero(posicion_fila, posicion_columna)
    posicion_fila, posicion_columna = mover(posicion_fila, posicion_columna)
    print()
    time.sleep(0.5)
"""


# Ejercicio 4: pedir al usuario que especifique en cada momento la fila y la columna en la cuál dibujar el "0"

FILAS = 6
COLUMNAS = 8

def dibujar_tablero(posicion_fila, posicion_columna):
    tablero = []
    for i in range(FILAS):
        fila = ["."] * COLUMNAS
        tablero.append(fila)

    tablero[posicion_fila][posicion_columna] = "0" # UNICA MODIFICACION
    for xx in tablero:
        print("  ".join(xx))


def mover(fila, columna):
    fila = int(input("Ingresar fila: "))
    columna = int(input("Ingresar columna: "))

    if fila > FILAS - 1:
        fila = 0
    if columna > COLUMNAS - 1:
        columna = 0

    return fila, columna


posicion_fila = 0
posicion_columna = 0
while True:
    dibujar_tablero(posicion_fila, posicion_columna)
    posicion_fila, posicion_columna = mover(posicion_fila, posicion_columna)
    print()
    time.sleep(0.5)

# Ejercicio 5: modificar el ejercicio anterior para que el usuario pueda mover el "0" utilizando las lwtras "a,w,d,s"
#              a: izquierda, w: arriba, d: derecha, s: abajo




