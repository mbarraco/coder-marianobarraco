# Ejemplo: calcular el promedio entre 6, 9 y 10 e imprimirlo por pantalla
mi_primer_valor = 6
mi_segundo_valor = 9
mi_tercer_valor = 10
mi_promedio = (mi_primer_valor + mi_segundo_valor + mi_tercer_valor) / 3
print("El promedio es:", mi_promedio)
print("El promedio es:")
print(mi_promedio)

# ejemplo 2 Funcion


def calcular_promedio():
    mi_primer_valor = 8
    mi_segundo_valor = 10
    promedio = (mi_primer_valor + mi_segundo_valor) / 2
    print("promedio es: ", promedio)


calcular_promedio()

# Repaso clase 1
mi_variable_numero = 1
mi_variable_texto = "uno mas uno"
mi_otra_variable_de_texto = ": es dos"
mi_texto_final = mi_variable_texto + mi_otra_variable_de_texto
print("." * 90)
print(mi_texto_final)
print("." * 90)
print(mi_texto_final[-8:])
print("." * 90)
print(type(mi_texto_final))
print("." * 90)

# Presentacion de tuplas y listas
mi_lista = [89, "ochenta y nueve", 12, -4, "t"]
mi_tupla = (89, "ochenta y nueve", 12, -4, "t")

print("_" * 90)
print(mi_lista)
print("_" * 90)
print(type(mi_lista))
print("_" * 90)
print(mi_tupla)
print("_" * 90)
print(type(mi_tupla))
print("_" * 90)

# Promedio con tuplas o listas
mis_notas = (10, 10, 8, 8)
mis_notas = [10, 10, 8, 8]
cantidad_de_notas = len(mis_notas)
suma_de_mis_notas = sum(mis_notas)
promedio = suma_de_mis_notas / cantidad_de_notas
print("cantidad de notas: ", cantidad_de_notas)
print("suma de mis notas: ", suma_de_mis_notas)
print("promedio", promedio)

print(mis_notas)
print(mis_notas[0])
print(mis_notas[0:2])
print(mis_notas[-3:])

# Ejemplo de agregar elementos "AL FINAL" de una lista: append
amigo_1 = "mariano"
amigo_2 = "el piti"
amigo_3 = "fer"
amigo_4 = "juan"
persona_1 = "roberto"
persona_2 = "valeria"
persona_3 = "romina"

fila_virtual = []
print("momento 1:", fila_virtual)
fila_virtual.append(persona_2)
print("momento 2:", fila_virtual)
fila_virtual.append(amigo_3)
print("momento 3:", fila_virtual)
fila_virtual.append(amigo_1)
print("momento 4:", fila_virtual)
fila_virtual.append(amigo_2)
print("momento 5:", fila_virtual)

print("la primer entrada es para:", fila_virtual[0])


# Ejemplo de que las listas son mutables - I
mis_notas = [10, 10, 8, 8]
mis_notas[1] = 7
print(mis_notas)

# Ejemplo de que las listas son mutables - II
mis_notas = [10, 10, 8, 8]
mis_notas[-2:] = ["A", "B+"]
print(mis_notas)


# Ejemplo de que las listas son mutables - III "borrar por slicing"
mis_notas = [10, 10, 8, 8]
mis_notas[-2:] = []
print(mis_notas)

# Pop
mis_notas = [10, 9, 8, 1]
print(mis_notas)
mis_notas.pop()
print(mis_notas)
print(len(mis_notas))

# Pop II
mis_notas = [10, 9, 8, 1]
print(mis_notas)
mis_notas.pop(1)
print(mis_notas)
print(len(mis_notas))

# Count
mis_notas = [10, 9, 8, 1,10, 9, 8, 1,10, 9, 8, 1,10, 9, 8, 1,10, 9, 8, 1]
print("la cantidad de 10 es: ",mis_notas.count(10))

# Listas anidadas
mi_gran_lista = []
mi_lista_chiquita = ["naruto", "saint seiya", "ranma 1/2"]
mi_tupla_chiquita = ("radiohead", "pearl jam", "audioslave")

print(mi_gran_lista)
print("la cantidad de elementos en mi gran lista es: ", len(mi_gran_lista)) # deberia ser 0
mi_gran_lista.append(mi_lista_chiquita)
print(mi_gran_lista) # debería ser ???
print("la cantidad de elementos en mi gran lista es: ", len(mi_gran_lista))
mi_gran_lista.append(mi_tupla_chiquita)
print(mi_gran_lista) # debería ser ???
print("la cantidad de elementos en mi gran lista es: ", len(mi_gran_lista))

# si quisiera imprimir en pantalla "audioslave"
print(mi_gran_lista[0])
print(mi_gran_lista[1])
print(mi_gran_lista[1][2])