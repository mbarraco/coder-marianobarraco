print(1 + 1 == 3)
print(9 / 3 == 3)
print(type(1 + 1 == 3))
print(type(9 / 3 == 3))

mi_valor_booleano = 1 + 1 == 3

print(f"mi valor booleano es {mi_valor_booleano}")
print()

mi_otro_valor_booleano = not mi_valor_booleano
print(f"mi OTRO valor booleano es {mi_otro_valor_booleano}")


xx = 3 > 4
yy = 2 < 11
zz = 3 <= 9 / 2
print()
print(xx, yy, zz)

# OR
xx = 3 > 4 or 1 == 1
yy = 2 < 11 or 1000 < 4
zz = 3 <= 9 / 2 or 1 == 1
ww = "b" > "z" or "d" > "z"
print()
print("OR:", xx, yy, zz, ww)


# AND
xx = 3 > 4 and 1 == 1
yy = 2 < 11 and 1000 < 4
zz = 3 <= 9 / 2 and 1 == 1
ww = "b" > "z" and "d" > "z"
print()
print("AND: ", xx, yy, zz, ww)


# LA COMPLICO
xx = not 3 > 4 and 1 == 1
yy = 2 < 11 or 1000 < 4
zz = 3 <= 9 / 2 or 1 == 1
ww = not "b" > "z" and not "d" > "z"

print()
print("LA COMPLICO: ", xx, yy, zz, ww)

# PRECEDENCIA DEL NOT
xx = not 3 > 4 and 1 == 1
yy = (not 3 > 4) and 1 == 1
zz = not (3 > 4 and 1 == 1)
print()
print("PRECEDENCIA DEL NOT: ", xx, yy, zz)
