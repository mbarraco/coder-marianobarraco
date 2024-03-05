intentos = 3
while intentos > 0:
    password = input("Di la palabra secreta amigo y entra: ")
    if password == "amigo":
        print("La puerta está abierta!")
        break
    intentos -= 1
    print(f"Intentos restantes: {intentos}")
    print()
else:
    print("Usuario bloqueado")
