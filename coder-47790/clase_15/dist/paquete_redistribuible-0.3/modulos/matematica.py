def sumar(a, b):
    return a + b

def dividir(a, b):
    return a / b


class Tablero:

    base = 8
    altura = 8

    def imprimir_tablero(self):

        filas = []
        for y in range(0, self.altura):
            fila = ["_"] * self.base

            print(fila)
            fila = "\t".join(fila)
            filas.append(fila)

        filas = "\n".join(filas)

        print(filas)

