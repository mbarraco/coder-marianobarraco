from paquete.tablero import *
from paquete.jugador import Jugador


mi_jugador = Jugador("Tamara", [9, 10])

tablero = Tablero([0, 0], [9, 10])


tablero.juego_finalizado(mi_jugador)