from pprint import pprint as pp


dict_1 = {}
dict_2 = {
    1: "uno",
    2: "dos"
}

print(dict_1)
print(dict_2)
print("-" * 90)

# Agregar valor a dict_1
dict_1[3] = "three"
print(dict_1)
print("-" * 90)

# Agregar valores
dict_1.update(dict_2)
print(dict_1)
print("-" * 90)