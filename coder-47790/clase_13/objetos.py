from pprint import pprint

class BaseDeDatos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.registro_de_usuarios = {}

    def guardar_usuario(self, usuario):
        self.registro_de_usuarios[usuario.email] = {
            "nombre": usuario.nombre,
            "password": usuario.password
        }

    def mostrar_registro(self):
        pprint(self.registro_de_usuarios)


class Usuario:
    def __init__(self, nombre, password, email):
        self.nombre = nombre
        self.password = password
        self.email = email

    def presentarse(self):
        print(f"Hola soy {self.nombre.upper()} y mi email es {self.email}")

    def __str__(self):
        return f"Soy {self.nombre}"


usuario_1 = Usuario("alberta", "admin1234", "beta@coder.com")
usuario_2 = Usuario("rodrigo", "admin1234", "rodri@coder.com")
usuario_3 = Usuario("leandra", "admin1234", "leandra@coder.com")

# usuario_1.presentarse()

base_de_datos = BaseDeDatos("users")
base_de_datos.mostrar_registro()
print("_" * 90)
base_de_datos.guardar_usuario(usuario_1)
base_de_datos.mostrar_registro()
print("_" * 90)
base_de_datos.guardar_usuario(usuario_2)
base_de_datos.mostrar_registro()
print("_" * 90)
base_de_datos.guardar_usuario(usuario_3)
base_de_datos.mostrar_registro()