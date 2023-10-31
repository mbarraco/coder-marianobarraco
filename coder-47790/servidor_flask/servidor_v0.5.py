from flask import Flask
from datetime import datetime

app = Flask("mi_servidor")


@app.route("/")
def home():
    mi_archivo = open("home.html", "r")
    contenido_html = mi_archivo.read()
    mi_archivo.close()
    return contenido_html


@app.route("/error")
def error():
    mi_archivo = open("archivo-que-no-existe", "r")
    contenido_html = mi_archivo.read()
    mi_archivo.close()
    return contenido_html


@app.route("/segundos")
def segundos():
    segundos = round(datetime.now().timestamp(), 1)
    return f"Hola!  desde el 1 de Enero de 1970 hasta este momento, pasaron: {segundos} segundos"


app.run(debug=True, port=8182)
