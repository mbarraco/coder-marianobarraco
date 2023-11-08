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



movimientos_permitidos = ["w", "a", "s", "d"]
while True:

    print(mi_jugador)
    if mi_tablero.juego_finalizado(mi_jugador):
        break

    movimiento = input(f"Hacia dónde debería moverse {mi_jugador.nombre}? {movimientos_permitidos} ")
    print("_" * 90)
    if movimiento not in movimientos_permitidos:
        print("Movimiento no permitido")
        continue

    if movimiento == "w":
        mi_jugador.caminar_arriba()
    elif movimiento == "a":
        mi_jugador.caminar_izquierda()
    elif movimiento == "s":
        mi_jugador.caminar_abajo()
    else:
        mi_jugador.caminar_derecha()

