

class Tablero2d:


    def __init__(self, filas, columnas, entrada):
        self.filas = filas
        self.columnas = columnas
        self.entrada = entrada


    def imprimir(self):
        una_fila = "_ " * self.columnas

        for i in range(0, self.filas):
            print(una_fila)



mi_tablero = Tablero2d(15, 4, [1,1])

print("_" * 90)
mi_tablero.imprimir()
print("_" * 90)
