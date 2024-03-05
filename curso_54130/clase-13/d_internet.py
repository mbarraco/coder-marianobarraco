# pip install flask
from flask import Flask, request

from b_banco import Banco
from a_entidades import Persona, Empresa


mi_banco = Banco("Interbank: el banco de internet")
persona_1 = Persona("alberto", 22123233, 89, "al@berto.com")
empresa_1 = Empresa("Compumundo hipermegared", "20-1312312-12","compumundo@mundo.com")
mi_banco.crear_cuenta(persona_1)
mi_banco.crear_cuenta(empresa_1)


app = Flask("Mi servidor")


@app.route("/")
def home():
    return f"bienvenidos a {mi_banco}"


@app.route("/cuentas")
def cuentas():
    return mi_banco.transformar_cuentas_en_texto()


app.run(debug=True, port=8081)
