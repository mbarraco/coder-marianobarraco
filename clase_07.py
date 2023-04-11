
mi_texto = "La rutA natURAL"
print(mi_texto.upper())
print(mi_texto.lower())
print(mi_texto.lower().upper())
print(mi_texto.title())
print(mi_texto.capitalize())

print("____________","cantidad de veces que aparece la letra 'R'")
print(mi_texto.count("R"))
print(mi_texto.upper().count("R"))

print("____________","dónde está la 'R'?")
print(mi_texto.find("R"))

print("____________","dónde está la última 'a'?")
print(mi_texto.rfind("a"))

print("____________","dónde está la primera 'a'?")
print(mi_texto.find("a"))

print("____________","así se separa el texto")
print(mi_texto.split(" "))
print(mi_texto.split("A"))
print(mi_texto.split("n"))

print("____________","así se juntan las cosas")
partes_del_nombre = ["greta", "van", "fleet"]
print(",".join(partes_del_nombre))
print(" -> ".join(partes_del_nombre))
print(" ".join(partes_del_nombre))
print(" ".join(partes_del_nombre).title())
print("".join(partes_del_nombre))

print("____________","así se 'limpian' las cosas")
numero_de_cliente = "#000000000025#0"
print(numero_de_cliente)
print(numero_de_cliente.strip())
print(numero_de_cliente.strip("#"))
print(numero_de_cliente.strip("#0"))

print("____________","así se reemplazan las partes de un string")
mi_otro_texto = "Freddie Mercury es el guitarrista de Queen"

print(mi_otro_texto)
print(mi_otro_texto.replace("guitarrista", "cantante"))
print(mi_otro_texto)


# Listas

# limpiar una lista
mi_lista = [1, "a", {1: "gato"}]
print(mi_lista)
mi_lista.clear()
print(mi_lista)

# extender una lista
mi_lista = [1, "a", {1: "gato"}]
mi_otra_lista = ["a", "b"]
print(mi_lista)
mi_lista.extend(mi_otra_lista)
print(mi_lista)

# forma alternativa
mi_lista = [1, "a", {1: "gato"}]
# extender una lista
mi_otra_lista = ["a", "b"]
print(mi_lista)
mi_lista = mi_lista + mi_otra_lista
print(mi_lista)

# Insertar elementos
mi_lista = [1, "a", {1: "gato"}]

print(mi_lista)
mi_lista.insert(2, "zz-top")
print(mi_lista)

# Invertir orden
mi_lista = [1, "a", {1: "gato"}]
print(mi_lista)
mi_lista.reverse()
print(mi_lista)

# Odenar elementos
mi_lista = ["a", "c" , "z", "b"]
print(mi_lista)
mi_lista.sort()
print(mi_lista)
mi_lista.sort(reverse=True)
print(mi_lista)
mi_lista.sort(reverse=False)
print(mi_lista)


# Ejemplo dialogo de pelicula
mi_texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
mis_lineas_de_texto = mi_texto.split("&")

for linea in mis_lineas_de_texto:
    print(linea)

print("." * 90)
for linea in mis_lineas_de_texto:
    print(linea.capitalize())

print("." * 90)

for indice, linea in enumerate(mis_lineas_de_texto):
    print(indice, linea.capitalize())

print("." * 90)
for linea in mis_lineas_de_texto:
    if linea[0] == "s" or linea[0] == "d":
        print("- " + linea.capitalize())
    else:
        print(linea.capitalize())

print("." * 90)
for indice, linea in enumerate(mis_lineas_de_texto):
    if indice == 0:
        print(linea.capitalize() + " ...")
    elif indice == 2:
        print("- " + linea.capitalize().replace("-", ""))
    else:
        print("- " + linea.capitalize())



# copia de conjuntos
mi_conjunto = {1, 2, 4, 5}
mi_copia = mi_conjunto.copy()
print(mi_copia)

# interseccion
A = {1, 2, 4, 5}
B = {1, 6, 7, 8}
print(A.isdisjoint(B))
print(B.isdisjoint(A))

# interseccion
A = {1, 2, 4, 5}
B = {1, 2}
print(A.issubset(B))
print(B.issubset(A))
print(A.issuperset(B))
print(B.issuperset(A))

# union
A = {1, 2, 4, 5}
B = {1, 2, "casa"}
print(A.union(B))
print(B.union(A))

# diferencia
A = {1, 2, 4, 5}
B = {1, 2, "casa"}
print(A - B)
print(B - A)
print(A.difference(B))
print(B.difference(A))

# diference update
A = {1, 2, 4, 5}
B = {1, 2, "casa"}
print(A.difference(B))
print(A)
print(A.difference_update(B))
print(A)

# interseccion
A = {1, 2, 4, 5}
B = {1, 2, "casa"}
print(A.intersection(B))
print(B.intersection(A))

# intersection_update
A = set([1, 2, 4, 5])
B = {1, 2, "casa"}
print(A.intersection_update(B))
print(A)

# Diccionarios!
mi_dict = {
    "coghlan": "edenor",
    "paternal": "edesur"
}

print("La empresa de distribucion electrica de Coghlan es")
print(mi_dict["coghlan"])

print("La empresa de distribucion electrica de Paternal es")
print(mi_dict.get("paternal"))

print("La empresa de distribucion electrica de Recoleta es")
print(mi_dict.get("recoleta", "No identificada"))

print("." * 90 )
for dato in mi_dict:
    print(dato)

print("." * 90 )
for clave, valor in mi_dict.items():
    print(f"la empresa del barrio {clave} es {valor}")

print("." * 90 )
print(mi_dict.keys())
print("recoleta" in mi_dict.keys())
print("paternal" in mi_dict.keys())

print("." * 90 )
print("edelap" in mi_dict.values())