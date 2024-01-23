mi_lista = [1, 5, 6, 7, "frodo", "sam", "merry"]

print("la lista es: ", mi_lista)

# Imprimir "frodo"
print(mi_lista[4])

# Calcular longitud
print("la longitud de la lista es: ", len(mi_lista))
print("la longitud del nombre 'frodo' es: ", len(mi_lista[4]))

# Reemplazar 1 elemento
mi_lista[3] = "Gandalf"
print("la nueva lista es: ", mi_lista)

# Reemplazar de a rebanadas (slices)
mi_lista[:2] = ["aragorn", "boromir"]
print("la nueva lista es: ", mi_lista)

# Concatenar otra lista
mi_otra_lista = ["Legolas", "Gimli"]
mi_lista = mi_lista + mi_otra_lista
print("la nueva lista es: ", mi_lista)


# Agregar 1 elemento
elemento = "Pippin"
mi_lista.append(elemento)
print("la nueva lista es: ", mi_lista)

# Remover un elemento
del mi_lista[2]
print("la nueva lista es: ", mi_lista)

# Agregar 1 elemento
elemento = "Luke Skywalker"
mi_lista.append(elemento)
print("la nueva lista es: ", mi_lista)

# Extraer el último
mi_personaje = mi_lista.pop()
print("la nueva lista es: ", mi_lista)
print("El personaje extraído es: ", mi_personaje)
