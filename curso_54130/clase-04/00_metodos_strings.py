mi_texto = "Cinco para los reyes enanos en sus casas de piedra"


posicion_1 = mi_texto.find("i")
posicion_2 = mi_texto.rfind("i")
print()
print("1 -> ", posicion_1)
print("2 -> ", posicion_2)

mi_experimento = mi_texto.split(" ")
mi_experimento_2 = mi_texto.split("en")
print("3 -> ", mi_experimento)
print("4 -> ", mi_experimento_2)

print()
mi_experimento_3 = "------".join(mi_experimento)
print("5 -> ", mi_experimento_3)

mi_experimento_3 = " ".join(mi_experimento)
print("6 -> ", mi_experimento_3)

print()
mi_experimento_4 = mi_texto.strip("reyes")
print("7 -> ", mi_experimento_4)
mi_experimento_4 = mi_texto.strip("piedra")
print("8 -> ", mi_experimento_4)
mi_experimento_4 = mi_texto.strip("Cinco")
print("9 -> ", mi_experimento_4)

print()
mi_experimento_5 = mi_texto.replace("reyes", "reinas")
print("10 --> ", mi_experimento_5)

mi_experimento_5 = mi_experimento_5.replace("los", "las")
print("11 --> ", mi_experimento_5)

mi_experimento_5 = mi_experimento_5.replace("casas de pi", "").replace(
    "enanos", "enanas"
)
print("12 --> ", mi_experimento_5)

mi_experimento_5 = mi_experimento_5.replace("e", "3")
print("13 --> ", mi_experimento_5)

mi_experimento_5 = mi_experimento_5.replace("a", "-")
print("14 --> ", mi_experimento_5)

print()
