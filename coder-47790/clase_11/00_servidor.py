# pip install Flask
# python 00_servidor.py
from flask import Flask, render_template_string, request  # Added 'request' here
from datetime import datetime
import json


app = Flask("mi_servidor")

@app.route('/')
def home():
    return 'Este es mi primer servidor! Bienvenidos'

@app.route('/saludo')
def saludo():
    return f'Hola!  desde el 1 de Enero de 1970 hasta este momento, pasaron: {datetime.now().timestamp()} segundos'


def registrar_usuario(user, password):
    mi_archivo = open("usuarios.json", "r")
    usuarios = json.load(mi_archivo)
    mi_archivo.close()

    mi_archivo = open("usuarios.json", "w")
    datos_a_guardar = {user: password}
    usuarios.update(datos_a_guardar)
    json.dump(usuarios, mi_archivo)
    mi_archivo.close()

@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    if request.method == "GET":
        return render_template_string('''
            <form action="/registrarse" method="post">  <!-- Changed action to /registrarse -->
                User: <input type="text" name="user"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" value="Submit">
            </form>
        ''')
    elif request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')

        registrar_usuario(user, password)

        return f"Muchas gracias {user}, fuiste registrado correctamente!"


app.run(debug=True, port=8182)
