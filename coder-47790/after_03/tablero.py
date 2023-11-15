class Tablero:

    longitud = 12

    def __init__(self, nombre, entrada, salida):

        if salida > self.longitud - 1:
            raise Exception("La salida tiene que ser menor o igual que la longitud")
        if entrada > self.longitud - 1:
            raise Exception("La entrada tiene que ser menor o igual que la longitud")
        if entrada < 0 or salida < 0:
            raise Exception("Entrada y Salida tienen que ser mayores que cero")
        if entrada == salida:
            raise Exception("Entrada y Salida tienen que ser distintas")

        self.entrada = entrada
        self.salida = salida
        self.nombre = nombre

    def imprimir(self):
        fila = ["_"] * self.longitud
        fila[self.entrada] = "E"
        fila[self.salida] = "S"

        print(" ".join(fila))
        # print(fila)

    def __str__(self):
        return f"Tablero {self.nombre}: <longitud> {self.longitud} <entrada> {self.entrada} <salida> {self.salida}"