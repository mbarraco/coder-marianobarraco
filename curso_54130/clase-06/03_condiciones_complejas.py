xx = int(input("Ingresar año de nacimiento: "))


# Silenciosa  : 1920 - 1940
# Boomer      : 1946 - 1964
# Generación X: 1965 - 1979
# Generación Y: 1980 - 2000
# Generación Z: 2001 - 2010

if xx >= 1920 and xx <= 1940:
    print()
    print("--Generación silenciosa")
    print()
elif xx > 1946 and xx <= 1964:
    print()
    print("--Generación boomer")
    print()
elif xx >= 1965 and xx <= 1979:
    print()
    print("--Generación X")
    print()
elif xx >= 1980 and xx <= 2000:
    print()
    print("--Generación Y")
    print()
elif xx >= 2001 and xx <= 2010:
    print()
    print("--Generación Z")
    print()
else:
    print()
    print("No existe generación asociada =)")
    print()
