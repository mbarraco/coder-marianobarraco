mis_usuarios = {}


def registrar_usuarios():
    while True:
        usuario = input("ingrese su usuario: ")
        password = input("ingrese su password: ")

        mis_usuarios[usuario] = password

        print(mis_usuarios)


def leer_usuario(usuario):
    pass


registrar_usuarios()
