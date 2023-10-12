
# mi_texto = "Nueve para los Reyes enanos en las casas de piedra"

# print(mi_texto.upper())
# print(mi_texto.lower())
# print(mi_texto.capitalize())
# print(mi_texto.title())

# print("count", mi_texto.count("a"))
# print("count", mi_texto.count("as"))
# print("count", mi_texto.count("as "))
# print("-" * 90)
# print("find", mi_texto.find("as "))
# print("rfind", mi_texto.rfind("as "))
# print("-" * 90)
# print("join", "<--->".join(["1", "2", "3"]))
# print("join", " ".join(["1", "2", "3"]))
# print("join", ", ".join(["1", "2", "3"]))
# print("join", "".join(["1", "2", "3"]))
# print("-" * 90)
# print("split", mi_texto.split(" "))
# print("split", mi_texto.split("e"))
# print("split", mi_texto.split("s "))
# print("-" * 90)
# print("split + join", " ".join(mi_texto.split("s "))) # desafio mental
# print("-" * 90)

mi_texto = "    Tres para los reyes Elfos   "
print(mi_texto)
print(mi_texto.strip(" "))
mi_texto = "...................Tres para los reyes Elfos......"
print(mi_texto)
print(mi_texto.strip("."))
print(mi_texto.strip(".").replace("e", "i"))
print(mi_texto.strip(".").lower().replace("e", "i"))