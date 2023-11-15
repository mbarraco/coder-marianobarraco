import math
import collections

mi_numero = 1/3

print(mi_numero)

print(math.ceil(mi_numero))
print(math.floor(mi_numero))

print(math.sqrt(9))
# print(math.sqrt(-4))

print("_" * 90)
mis_notas = [5, 6, 6, 2, 3, 10, 10, 5, 6]

mi_contador = collections.Counter(mis_notas)
print(mi_contador)

mi_texto = "abaracadabra pata de cabra"
mi_contador_2 = collections.Counter(mi_texto)
print(mi_contador_2)

print(mi_contador_2.most_common(1))