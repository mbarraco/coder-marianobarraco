import time

tablero = []
for i in range(5):
    # time.sleep(1)
    # print(tablero)
    fila = []
    for j in range(3):
        fila.append(".")  # fila -> [".", ".", "."]
    tablero.append(
        fila
    )  # tablero -> [[".", ".", "."], [".", ".", "."], [".", ".", "."], [".", ".", "."], [".", ".", "."]]

# print(tablero)

for xx in tablero:
    time.sleep(1)
    # print(xx)
    print("  ".join(xx))
