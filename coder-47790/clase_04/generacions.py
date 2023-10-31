# edad = int(input(":"))  # Alternativa

fecha_de_nacimiento = input("\nIngrese un valor para la fecha_de_nacimiento: ")
if not fecha_de_nacimiento.isnumeric():
    print("Por favor ingrese un número entero")
else:
    xx = int(fecha_de_nacimiento)

    if xx >= 1920 and xx <= 1940:
        print("Generacion Silenciosa")
    elif xx >= 1946 and xx <= 1964:
        print("Generacion BB")
    elif xx >= 1965 and xx <= 1979:
        print("Generacion X")
    elif xx >= 1980 and xx <= 2000:
        print("Generacion Y")
    elif xx >= 2001 and xx <= 2010:
        print("Generacion Z")
    else:
        print("Fuera de rango de fecha_de_nacimiento")
