"mi duda es lo que pusiste arriba no escuche bien el IMPORT par que sirve"
from pprint import pprint as pp  # para esta clase no importa saberlo


mi_lista_1 = []
mi_lista_2 = [1, 2, 3]
mi_lista_3 = ["a", "b", "c"]
mi_lista_anidada = [mi_lista_1, mi_lista_2, mi_lista_3]

print(mi_lista_1)
print(mi_lista_2)
print(mi_lista_3)
pp(mi_lista_anidada)


print(f"La primer letra de mi appelido es '{mi_lista_3[1]}'")
print(f"La primer letra de mi appelido es '{mi_lista_anidada[2]}'")
print(f"La primer letra de mi appelido es '{mi_lista_anidada[2][1]}'")
