# pip install flask
from flask import Flask, request, render_template_string

from b_banco import Banco
from a_entidades import Persona, Empresa


mi_banco = Banco("Felipe's Bank")
persona_1 = Persona("rogelia", 999, 34, "rogelia@gmail.com")
persona_2 = Persona("edgar", 777, 79, "edgar@gmail.com")
empresa_1 = Empresa("Nerv", 3434, "ikari@nerv.com")

mi_banco.crear_cuenta(persona_1)
mi_banco.crear_cuenta(persona_2)
mi_banco.crear_cuenta(empresa_1)

mi_banco.depositar_en_cuenta(persona_1, 100)
mi_banco.depositar_en_cuenta(persona_1, 94)
mi_banco.depositar_en_cuenta(persona_1, -70)
mi_banco.depositar_en_cuenta(persona_2, 1000)
mi_banco.depositar_en_cuenta(persona_2, -700)
mi_banco.depositar_en_cuenta(empresa_1, 14000000)


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
            <form action="/xxxxx" method="post">
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


@app.route("/xxxxx", methods=['POST'])
def crear_cuenta():
    print("-----------------------------------request.form")
    print(request.method)
    print(request.form)
    print("-----------------------------------request.form")
    tipo_de_cuenta = request.form["tipo_cuenta"]
    nombre = request.form["nombre"]
    identificador = request.form["identificador"]
    email  = request.form["email"]
    edad = request.form["edad"]

    if tipo_de_cuenta == "persona":
        cliente = Persona(nombre, identificador, edad, email)
    else:
        cliente = Empresa(nombre, identificador, email)

    mi_banco.crear_cuenta(cliente)
    return f"La cuenta para  {nombre} fue creada correctamente", 201


app.run(debug=True, port=8000)
