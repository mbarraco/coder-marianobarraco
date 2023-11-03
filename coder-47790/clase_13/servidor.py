from flask import Flask, request  # Added 'request' here
from datetime import datetime

class BaseDeDatos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.registro_de_usuarios = {}

    def guardar_usuario(self, usuario):
        self.registro_de_usuarios[usuario.email] = {
            "nombre": usuario.nombre,
            "password": usuario.password
        }

    def obtener_usuario(self, email):
        return self.registro_de_usuarios[email]

    def mostrar_registro(self):
        return self.registro_de_usuarios


class Usuario:
    def __init__(self, nombre, password, email):
        self.nombre = nombre
        self.password = password
        self.email = email

    def presentarse(self):
        print(f"Hola soy {self.nombre.upper()} y mi email es {self.email}")

    def __str__(self):
        return f"Soy {self.nombre}"


app = Flask("mi_servidor")
base_de_datos = BaseDeDatos("users")


@app.route("/")
def home():
    mi_archivo = open("home.html", "r")
    contenido_html = mi_archivo.read()
    mi_archivo.close()
    return contenido_html


@app.route("/tipos-de-request")
def tipos_de_request():
    metodo = request.method
    return f"Hola! el tipo de pedido fue: {metodo}"


@app.route("/usuario", methods=["GET", "POST"])
def tipos_de_request_4():
    metodo = request.method

    if metodo == "GET":
        return f""" El tipo de pedido fue <h1>{metodo}</h1>
                    <form action="/usuario" method="post">
                        User: <input type="text" name="user"><br>
                        Password: <input type="password" name="password"><br>
                        email: <input type="email" name="email"><br>
                        <input type="submit" value="Guardar usuario">
                    </form>
                """
    else:
        user = request.form.get("user")
        password = request.form.get("password")
        email = request.form.get("email")

        usuario = Usuario(user, password, email)
        base_de_datos.guardar_usuario(usuario)

        # return f""" El tipo de pedido fue <h1>{metodo}</h1>. <br>
        #             {base_de_datos.mostrar_registro()}
        #         """

        respuesta = f"El tipo de pedido fue <h1>{metodo}</h1>"

        for registro in base_de_datos.registro_de_usuarios.items():
            respuesta += "<br>"
            respuesta += f"{registro}"

        return respuesta


app.run(debug=True, port=8182)
