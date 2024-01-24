mi_lista = ["a", "b", "a", "a", "b"]

# contar ocurrencias
ocurrencias = mi_lista.count("a")
print("la letra 'a' aparece: ", ocurrencias, " veces")
ocurrencias = mi_lista.count("b")
print("la letra 'b' aparece: ", ocurrencias, " veces")
ocurrencias = mi_lista.count("c")
print("la letra 'c' aparece: ", ocurrencias, " veces")
print("la letra 'c' aparece: ", mi_lista.count("c"), " veces")


# Averiguar en qué posición está tal elemento
posicion = mi_lista.index("a")
print("la letra 'a' está en la posición: ", posicion)
posicion = mi_lista.index("b")
print("la letra 'b' está en la posición: ", posicion)
posicion = mi_lista.index("XXXXXXXX")
print("la letra 'XXXXXXXX' está en la posición: ", posicion)