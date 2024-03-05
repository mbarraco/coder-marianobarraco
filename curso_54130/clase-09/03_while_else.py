intentos = 3
while True:
    if intentos == 0:
        print("Usuario bloqueado")
        break

    password = input("Di la palabra secreta amigo y entra: ")
    if password == "amigo":
        print("La puerta está abierta!")
        break
    intentos -= 1
    print(f"Intentos restantes: {intentos}")
    print()
