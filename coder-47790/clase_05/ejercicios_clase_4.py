# edad = input("Ingresar edad: ")
# edad = int(edad)

edad = input("Ingresar edad: ")
antiguedad = input("Ingresar antiguedad: ")
ingreso = input("Ingresar ingreso: ")

if not (edad.isnumeric() and antiguedad.isnumeric() and ingreso.isnumeric()):
    print(
        f"Por favor ingrese un valor numérico. Usted ha ingresado: {edad}, {antiguedad}, {ingreso}"
    )
else:
    print(f"---->  0")
    edad = int(edad)
    antiguedad = int(antiguedad)
    ingreso = int(ingreso)

    if edad < 18:
        print(f"---->  1")
        print("Credito denegado")
    else:
        print(f"---->  2")
        if antiguedad >= 3 and ingreso >= 2500:
            print(f"---->  3")
            print("Credito aprobado!")
        elif antiguedad < 3 and ingreso >= 4000:
            print(f"---->  4")
            print("Credito aprobado!")
        else:
            print(f"---->  5")
            print("Credito denegado")
