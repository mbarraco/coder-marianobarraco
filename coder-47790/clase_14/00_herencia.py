
class Padre:
    def __init__(self, nombre):
        self.nombre = nombre

class BaseDeDatos(Padre):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.registro_de_usuarios = {}

    def guardar_usuario(self, usuario):
        if usuario.email in self.registro_de_usuarios.keys():
            print(f"Error, ya existe un registro con ese email: {usuario.email}")
            return

        self.registro_de_usuarios[usuario.email] = {
            "nombre": usuario.nombre,
            "password": usuario.password
        }

    def obtener_usuario(self, email):
        return self.registro_de_usuarios[email]

    def __str__(self):
        return f"Soy la base de datos {self.nombre} y tengo {len(self.registro_de_usuarios)} registros"


class Usuario(Padre):
    def __init__(self, nombre, password, email):
        super().__init__(nombre)
        self.password = password
        self.email = email

    def presentarse(self):
        print(f"Hola soy {self.nombre.upper()} y mi email es {self.email}")

    def __str__(self):
        return f"Soy {self.nombre} y mi correo es {self.email}"


usuario_1 = Usuario("alberto", "pass1234", "a@a.com")
base_de_datos = BaseDeDatos("mi-base-de-datos")
base_de_datos.guardar_usuario(usuario_1)


# print(usuario_1)
# print(base_de_datos)

print(usuario_1.nombre)
print(base_de_datos.nombre)