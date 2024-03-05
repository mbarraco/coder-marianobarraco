# Muchachos, quede con la duda del find y el index,
# encuentran el primer carácter del string,
# si quiero que encuentre el segundo entonces no sirve?

mi_texto = "Lionel messi, campeón del mundo"

print(mi_texto.find("i", 1))
print(mi_texto.find("i", 2))
print(mi_texto.find("l"))
print(mi_texto.find("L"))
print()
print(mi_texto.capitalize())
print(mi_texto.title())
print(mi_texto.upper())
print(mi_texto.lower())
print(mi_texto.lower().title())

print()
algo_asi = ["Lionel", "messi", "campeón", "del", "mundo"]
print(algo_asi)

xx = mi_texto.split(" ")
print(xx)

xx = mi_texto.split("messi")
print(xx)

print()
mi_texto = "El rápido zorro marrón salta sobre el perro perezoso"
xx = mi_texto.split(" ")
print(xx.index("rápido"))

print()
mi_texto = "El rápido zorro marrón salta sobre el perro perezoso"
xx = mi_texto.split("rápido")
print(xx[1])
