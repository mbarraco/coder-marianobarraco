mi_numero = 505


def saludar():
    print("hola!")


def saludar_2():
    print(f"mi_numero es {mi_numero}")


def xx():
    print("_" * 90)


def xx_2(cantidad_de_separadores):
    print("_" * cantidad_de_separadores)


def xx_3(cantidad, separador):
    print(separador * cantidad)


def xx_4(cantidad=90, separador="_"):
    print(separador * cantidad)


# saludar()
# xx()
# saludar_2()

# xx_2(90)
# xx_2(105)

# xx_3(50, "i")
# xx_4(15)
# xx_4(15, ">")
# xx_4()