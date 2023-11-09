class Jugador:

    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion

    def __str__(self):
        return f"Jugador: {self.nombre}, posición: {self.posicion}"