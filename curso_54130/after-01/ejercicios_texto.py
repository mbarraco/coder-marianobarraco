mi_texto = "El rápido zorro marrón salta sobre el perro perezoso"


# 1. Extraer la primer letra "p" del texto e imprimirla
print("1 --> (luciano)", mi_texto[5:6])
print("1 --> (dante) ", mi_texto[5])

posicion_de_la_letra_p = mi_texto.index("p")
print("1 --> (mariano)", mi_texto[posicion_de_la_letra_p])

xx = mi_texto.find("p")
print("1 --> (mariano)", mi_texto[xx])

# 2. Extraer la palabara "rápido" del texto e imprimirla
print()
print("2 --> (mariano)", mi_texto[3:9])


# 3. Voltear el texto e imprimirlo
print()
print("3 -->  ", mi_texto[::-1])

# 4 Extraer los últimos 7 caracteres del texto
print()
print("4 -->  ", mi_texto[-7:])
