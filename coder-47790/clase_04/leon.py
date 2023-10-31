año_de_nacimiento = int(input("ingrese su año de nacimiento: "))

if not año_de_nacimiento.isnumeric():
    print("ingrese su año de nacimiento en numeros por favor.")
else:
    print(f"la edad ingresada es {año_de_nacimiento}")
if año_de_nacimiento >= 1920:
    print("usted es generacion Silenciosa")
elif año_de_nacimiento <= 1940:
    print("usted es generacion Silenciosa")
