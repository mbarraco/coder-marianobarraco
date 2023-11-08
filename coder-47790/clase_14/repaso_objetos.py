




class BaseDeDatos:
    def __init__(self, nombre):
        self.nombre = nombre
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


class Usuario:
    def __init__(self, nombre, password, email):
        self.nombre = nombre
        self.password = password
        self.email = email

    def presentarse(self):
        print(f"Hola soy {self.nombre.upper()} y mi email es {self.email}")

    def __str__(self):
        return f"Soy {self.nombre} y mi correo es {self.email}"


usuario_1 = Usuario("alberto", "pass1234", "a@a.com")
usuario_2 = Usuario("agustina", "pass1234", "a@a.com.ar")
usuario_3 = Usuario("raquel", "pass1234", "a@a.com")
base_de_datos = BaseDeDatos("mi-base-de-datos")
print(base_de_datos)

print("_" * 90)
base_de_datos.guardar_usuario(usuario_1)
base_de_datos.guardar_usuario(usuario_2)
base_de_datos.guardar_usuario(usuario_3)
print(base_de_datos)

print("_" * 90)
otra_base_de_datos = BaseDeDatos("la-otra-base-de-datos")
otra_base_de_datos.guardar_usuario(usuario_1)
print(otra_base_de_datos)

