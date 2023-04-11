
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