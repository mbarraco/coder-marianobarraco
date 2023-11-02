from flask import Flask, request  # Added 'request' here
from datetime import datetime

app = Flask("mi_servidor")





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
                        <input type="submit" value="Submit">
                    </form>
                """
    else:
        user = request.form.get("user")
        password = request.form.get("password")

        return f""" El tipo de pedido fue <h1>{metodo}</h1>. <br>
                La información enviada fue
                <table border="1">
                    <tr>
                        <td>user</td>
                        <td>{user}</td>
                    </tr>
                    <tr>
                        <td>password</td>
                        <td>{password}</td>
                    </tr>
                </table>


                """


app.run(debug=True, port=8182)
