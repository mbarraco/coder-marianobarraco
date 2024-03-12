# pip install flask
from flask import Flask, request, render_template_string

from b_banco import Banco
from a_entidades import Persona, Empresa



mi_banco = Banco("Matías Bank")
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



app = Flask("Mi servidor")


@app.route("/")
def home():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Welcome to my bank</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                flex-direction: column;
            }
            h1 {
                color: #333;
            }
            a {
                display: inline-block;
                background-color: #007bff;
                color: white;
                padding: 10px 20px;
                margin: 10px;
                border-radius: 5px;
                text-decoration: none;
                transition: background-color 0.3s ease;
            }
            a:hover {
                background-color: #0056b3;
            }
            .container {
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bienvenidos a Interbank: el banco de internet</h1>
            <a href="/crear-cuenta-form">Crear Cuenta Nueva</a>
            <a href="/cuentas">Ver Cuentas</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)


@app.route("/cuentas")
def cuentas():
    cuentas_dict = mi_banco.mostrar_todas_las_cuentas()
    cuentas_html = ""
    for identificador, saldo in cuentas_dict.items():
        cuentas_html += f"<li>La cuenta {identificador} tiene saldo: {saldo}</li>"

    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Lista de Cuentas</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                flex-direction: column;
            }}
            h1 {{
                color: #333;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                background-color: #fff;
                margin: 5px 0;
                padding: 10px;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            a {{
                display: inline-block;
                background-color: #007bff;
                color: white;
                padding: 10px 20px;
                margin: 10px;
                border-radius: 5px;
                text-decoration: none;
                transition: background-color 0.3s ease;
            }}
            a:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div>
            <h1>Lista de Cuentas</h1>
            <ul>{cuentas_html}</ul>
            <a href="/">Volver al Inicio</a>
        </div>
    </body>
    </html>
    '''
    return html_content


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
    tipo_cuenta = request.form.get("tipo_cuenta")
    identificador = request.form.get("identificador")

    email = request.form.get("email")

    if tipo_cuenta == "persona":
        edad = request.form.get("edad")
        nombre = request.form.get("nombre")
        cliente = Persona(nombre, identificador, edad, email)
    else:
        cliente = Empresa(nombre, identificador, email)

    mi_banco.crear_cuenta(cliente)
    response = f'''
    <!DOCTYPE html>
        <html>
        <head>
            <title>Account Creation Success</title>
        </head>
        <body>
            <p>Account for {nombre} created successfully</p>
            <a href="/crear_cuenta_form">Create Another Account</a><br>
            <a href="/cuentas">View All Accounts</a>
        </body>
        </html>
    '''
    return response, 201

app.run(debug=True, port=8081)
