

lista_1 = []
lista_2 = list()

# print(lista_1)
# print(lista_2)
# print("-" * 10)

lista_1.append(56789)
lista_1.append("Hello world")

lista_2.append("Hola y Adios!")
lista_2.append(5555)

lista_2.extend(
    ["alfa", "beta"]
    )

lista_2.append(
    ["alfa", "beta"]
    )

# print(lista_1)
# print(lista_2)
# print("-" * 10)

lista_3 = lista_1[:-1]
# lista_3_mal_armada = lista_1.pop()
lista_4 = lista_2[1:-1]
lista_4_alternativa = lista_2[1:len(lista_2)-1]
lista_5 = lista_4 + lista_3

# print(lista_1)
# print(lista_2)
# print(lista_3)
# print(lista_3_mal_armada)
# print(lista_4)
# print(lista_4_alternativa)
# print(lista_5)
# print("-" * 10)

print(f"Lista 1: {lista_1}")
print(f"Lista 2: {lista_2}")
print(f"Lista 3: {lista_3}")
print(f"Lista 4: {lista_4}")
print(f"Lista 5: {lista_5}")


print("Lista 1: {lista_1}")
print("Lista 2: {lista_2}")
print("Lista 3: {lista_3}")
print("Lista 4: {lista_4}")
print("Lista 5: {lista_5}")
