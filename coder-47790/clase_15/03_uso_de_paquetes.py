from random import randint

from paquete.tablero import *
from paquete.jugador import Jugador


tablero = Tablero([0, 0], [9, 10])

xx = randint(0, tablero.base - 1)
yy = randint(0, tablero.altura - 1)

mi_jugador = Jugador("Tamara", [xx, yy])

tablero.juego_finalizado(mi_jugador)