mi_lista = [1, 3, 4]
mi_tupla = (1, 3, 4)
mi_numero = 9

print(mi_lista)
print(mi_tupla)
print(mi_numero)

print("-------------------")
print(
    type(mi_lista)
)
print(
    type(mi_tupla)
)
print(
    type(mi_numero)
)
print("-------------------")
mi_otra_lista = tuple(mi_lista)
print(mi_otra_lista)
print(type(mi_otra_lista))

print("-------------------")
mi_otro_numero = str(mi_numero)
print(mi_otro_numero)
print(type(mi_otro_numero))