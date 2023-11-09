from paquete_redistribuible.jugador import Jugador
from paquete_redistribuible.tablero import Tablero


mi_jugador = Jugador("Alex", [1, 2])
mi_tablero = Tablero([0,0], [1,2])
print(mi_jugador)
print(mi_tablero)

mi_tablero.juego_finalizado(mi_jugador)