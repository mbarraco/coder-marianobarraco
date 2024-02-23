
registro = {}

def registrar():
    usuario = input("Elegir un nombre de usuario: ")
    password = input("Elegir una contraseña: ")
    registro[usuario] = password

registrar()


print(registro)

def loggear():
    usuario = input("Ingresar un nombre de usuario: ")
    password = input("Ingresar una contraseña: ")

    print("Has ingresado con éxito!")
    print("Contraseña incorrecta!")


loggear()

"""En la función loggear falta decidir si el par usuario/password son
correctos.

para eso podríamos inspirarnos en esto:

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




"""