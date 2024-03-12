# pip install flask
from flask import Flask, request, render_template_string

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

@app.route("/crear-cuenta-form")
def crear_cuenta_form():
    # Simple HTML form
    html_form = '''
    <html>
        <body>
            <form action="/crear_cuenta" method="post">
                <label for="tipo_cuenta">Tipo de cuenta:</label><br>
                <select name="tipo_cuenta" id="tipo_cuenta">
                    <option value="persona">Persona</option>
                    <option value="empresa">Empresa</option>
                </select><br><br>

                <label for="nombre">Nombre:</label><br>
                <input type="text" id="nombre" name="nombre"><br><br>

                <label for="identificador">Documento/Identificador:</label><br>
                <input type="text" id="identificador" name="identificador"><br><br>

                <label for="edad">Edad (solo personas):</label><br>
                <input type="text" id="edad" name="edad"><br><br>

                <label for="email">Email:</label><br>
                <input type="email" id="email" name="email"><br><br>

                <input type="submit" value="Crear Cuenta">
            </form>
        </body>
    </html>
    '''
    return render_template_string(html_form)


@app.route("/crear_cuenta", methods=['POST'])
def crear_cuenta():
    print(request.form)
    return f"Estamos trabajando para usted", 201

app.run(debug=True, port=8081)
