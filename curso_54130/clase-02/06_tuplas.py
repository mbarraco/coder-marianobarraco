mi_lista = ["a", "b", "c"]
mi_tupla = ("a", "b", "c")


print("mi_lista", mi_lista)
print("mi_tupla", mi_tupla)

mi_lista[1] = 99
mi_lista.append("9999")
# mi_tupla[1] = 99 NO SE PUEDE HACER
# mi_tupla.append("9999") NO SE PUEDE HACER
# mi_tupla.clear() NO SE PUEDE HACER

print()
print("mi_lista", mi_lista)
print("mi_tupla", mi_tupla)
