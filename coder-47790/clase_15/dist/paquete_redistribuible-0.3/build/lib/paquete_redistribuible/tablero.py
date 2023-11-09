class Tablero:

    altura = 8
    base = 8

    def __init__(self, entrada, salida):
        self.entrada = entrada
        self.salida = salida

    def juego_finalizado(self, jugador):
        if jugador.posicion == self.salida:
            print("Juego finalizado: el jugador llegó a la salida")
            return True
        else:
            print("Juego no finalizado")
            return False


    def __str__(self):
        return f"Tablero: {self.entrada}, {self.salida}"