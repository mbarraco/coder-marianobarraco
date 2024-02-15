
# 1
for i in "cordoba":
    print(i)
print()

# 2
for i in [66,55,55,44]:
    print(i)
print()

# 3
for i in range(2, 9):
    print(i)
print()

# 4
posicion = 0
for i in "cordoba":
    print(f"{posicion}) {i}")
    posicion = posicion + 1  # posicion += 1
print()

# 5
for posicion, letra in enumerate("cordoba"):
    print(f"{posicion}) {letra.upper()}")
print()