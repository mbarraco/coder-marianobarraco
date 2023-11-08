
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


    def __len__(self):
        return len(self.registro_de_usuarios)

    def __getitem__(self, xx):
        return self.registro_de_usuarios.get(xx, f"No encontrado: {xx}")



class Usuario:
    def __init__(self, nombre, password, email):
        self.nombre = nombre
        self.password = password
        self.email = email

    def presentarse(self):
        print(f"Hola soy {self.nombre.upper()} y mi email es {self.email}")

    def __str__(self):
        return f"Soy {self.nombre} y mi correo es {self.email}"


base_de_datos = BaseDeDatos("mi-base-de-datos")
print(base_de_datos)
print(len(base_de_datos))
print("_" * 90)

usuario_1 = Usuario("alberto", "pass1234", "a@a.com")
usuario_2 = Usuario("agustina", "pass1234", "b@a.com.ar")
usuario_3 = Usuario("raquel", "pass1234", "raquel@a.com.es")

base_de_datos.guardar_usuario(usuario_1)
base_de_datos.guardar_usuario(usuario_2)
base_de_datos.guardar_usuario(usuario_3)

print(base_de_datos)
print(len(base_de_datos))
print("_" * 90)

usuario_1 = Usuario("alberto", "pass1234", "xxa@a.com")
usuario_2 = Usuario("agustina", "pass1234", "xxb@a.com.ar")
usuario_3 = Usuario("raquel", "pass1234", "xxraquel@a.com.es")

base_de_datos.guardar_usuario(usuario_1)
base_de_datos.guardar_usuario(usuario_2)
base_de_datos.guardar_usuario(usuario_3)

print(base_de_datos)
print(len(base_de_datos))
print("_" * 90)


print(base_de_datos["xxa@a.com"])
print(base_de_datos["p@p.com"])
print(base_de_datos["f@f.com"])
usuario_5 = Usuario("raquel", "pass1234", "f@f.com")
base_de_datos.guardar_usuario(usuario_5)
print(base_de_datos["f@f.com"])

