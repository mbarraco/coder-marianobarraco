mi_lista = ["A", "B", "C"]
mi_otra_lista = ["a", "b", "c"]

print()
print("1 -> ", mi_lista)
print("2 -> ", mi_otra_lista)
print()

# EXTEND
mi_lista.append("gandalf")
print("3 -> ", mi_lista)
mi_lista.extend(mi_otra_lista)
print("4 -> ", mi_lista)
print()

# INSERT
mi_lista.insert(0, "frodo")
print("5 -> ", mi_lista)

mi_lista.insert(1, "bilbo")
print("6 -> ", mi_lista)

mi_lista.insert(3, "elrond")  # insertar en la 4ta posición
print("7 -> ", mi_lista)

# Reverse
print()
mi_lista.reverse()
print("8 -> ", mi_lista)

# Sort
print()
mi_lista.sort()
print("8 -> ", mi_lista)

print()
