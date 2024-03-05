# print("123")
# print(type("12312"))
# print(type(4))
# print(len("mi nombre es Legolas"))

lista_funciones_ejecutadas = ["print", "print", "print", "print", "type", "type", "len"]
conjunto_de_funciones_ejecutadas = set(
    ["print", "print", "print", "print", "type", "type", "len"]
)

lista = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3]
conjunto = {1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3}

# IN
print()
print("está el 99 en la lista?   ", 99 in lista)
print("está el 1 en el conjunto?", 1 in conjunto)
print()

print()
print("lista   ", lista_funciones_ejecutadas)
print("conjunto", conjunto_de_funciones_ejecutadas)
print()
print("lista   ", lista)
print("conjunto", conjunto)
print()

# Agregar
conjunto.add(6)
conjunto.add(7)
conjunto.add(8)
conjunto.update(("frodo", "sam", "pippin", "merry"))
print("1 ->", "conjunto", conjunto)
print()

# remover
conjunto.remove(7)
print("2 ->", "removi el 7", conjunto)
print()

# longitud
print("3 ->", "longitud", len(conjunto))
print()

# discard
conjunto.discard("gandalf")
conjunto.discard(1)
print("4 ->", "descartar", conjunto)
print()


# descartar elementos aleatorios
elemento = conjunto.pop()
print("5 ->", "elemento al azar:", elemento)
print("5 ->", "el conjunto:", conjunto)
print()
elemento = conjunto.pop()
print("6 ->", "elemento al azar:", elemento)
print("6 ->", "el conjunto:", conjunto)
print()
elemento = conjunto.pop()
print("7 ->", "elemento al azar:", elemento)
print("7 ->", "el conjunto:", conjunto)
print()
