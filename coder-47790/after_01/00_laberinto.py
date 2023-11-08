class Tablero:

    altura = 8
    base = 8

    def __init__(self, entrada, salida):
        self.entrada = entrada
        self.salida = salida

    def juego_finalizado(self, jugador):
        if jugador.posicion == self.salida:
            print("Juego finalizado: el jugador llegó a la salida")
        else:
            print("Juego no finalizado")

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


mi_tablero = Tablero([1,1], [5,4])
mi_jugador = Jugador("Frodo", mi_tablero.entrada)

print(mi_tablero)
print("_" * 90)
print(mi_jugador)
print("_" * 90)

# si, hasta aca entendí, pero ahora como avanza en el tablero?
mi_jugador.caminar_derecha()
print(mi_jugador)
mi_tablero.juego_finalizado(mi_jugador)
print("_" * 90)

mi_jugador.caminar_arriba()
print(mi_jugador)
mi_tablero.juego_finalizado(mi_jugador)
print("_" * 90)


mi_jugador.caminar_arriba()
mi_jugador.caminar_arriba()
mi_jugador.caminar_derecha()
mi_jugador.caminar_derecha()
mi_jugador.caminar_derecha()
print(mi_jugador)
mi_tablero.juego_finalizado(mi_jugador)
print("_" * 90)
