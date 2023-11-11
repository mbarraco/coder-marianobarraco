import os


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


    # def imprimir(self, jugador):
    #     print("\033c") # Esto es para MAC (apple),
    #     # os.system('cls') # Esto es para windows

    #     x_jugador = jugador.posicion[0]
    #     y_jugador = self.altura - jugador.posicion[1] - 1

    #     x_salida = self.salida[0]
    #     y_salida = self.altura - self.salida[1] - 1

    #     for y in range(0, self.altura):
    #         fila = ["_"] * self.base
    #         if y == y_jugador:
    #             fila[x_jugador] = "0"
    #         if y == y_salida:
    #             fila[x_salida] = "X"

    #         # print(fila)
    #         print("\t".join(fila))

    def imprimir_html(self, jugador):

        x_jugador = jugador.posicion[0]
        y_jugador = jugador.posicion[1]

        x_salida = self.salida[0]
        y_salida = self.salida[1]

        filas = []
        for y in range(0, self.altura):
            fila = ["_"] * self.base
            if y == y_jugador:
                fila[x_jugador] = "0"
            if y == y_salida:
                fila[x_salida] = "X"

            print(fila)
            fila = "\t".join(fila)
            filas.append(fila)
        filas.reverse(  )

        # import ipdb; ipdb.set_trace()
        return "</br>".join(filas)

    def __str__(self):
        return f"Tablero: <entrada> {self.entrada}, <salida> {self.salida}"


class Jugador:

    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion

    def caminar_arriba(self):
        self.posicion[1] += 1

    def caminar_abajo(self):
        self.posicion[1] -= 1

    def caminar_izquierda(self):
        self.posicion[0] -= 1

    def caminar_derecha(self):
        self.posicion[0] += 1

    def __str__(self):
        return f"La posicion de {self.nombre.title()} es {self.posicion}"


class Juego:

    def __init__(self):
        self.tablero = Tablero([0,0], [5,4])
        self.jugador = Jugador("Frodo", self.tablero.entrada)

    def registrar_jugada(self, jugada):
        if self.tablero.juego_finalizado(self.jugador):
            return
        if jugada == "w":
            self.jugador.caminar_arriba()
        elif jugada == "a":
            self.jugador.caminar_izquierda()
        elif jugada == "s":
            self.jugador.caminar_abajo()
        else:
            self.jugador.caminar_derecha()

    def finalizado(self):
        return self.tablero.juego_finalizado(self.jugador)

    def obtener_tablero_actual(self):
        return self.tablero.imprimir_html(self.jugador)

