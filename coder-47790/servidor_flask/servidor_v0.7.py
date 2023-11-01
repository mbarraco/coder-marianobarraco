from flask import Flask, request  # Added 'request' here
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


@app.route("/tipos-de-request")
def tipos_de_request():
    metodo = request.method
    return f"Hola! el tipo de pedido fue: {metodo}"


@app.route("/tipos-de-request-2")
def tipos_de_request_2():
    metodo = request.method

    return f""" El tipo de pedido fue <h1>{metodo}</h1>
                <form action="/tipos-de-request-2" method="post">
                    User: <input type="text" name="user"><br>
                    Password: <input type="password" name="password"><br>
                    <input type="submit" value="Submit">
                </form>
            """


@app.route("/tipos-de-request-3", methods=["GET", "POST"])
def tipos_de_request_3():
    metodo = request.method

    return f""" El tipo de pedido fue <h1>{metodo}</h1>
                <form action="/tipos-de-request-3" method="post">
                    User: <input type="text" name="user"><br>
                    Password: <input type="password" name="password"><br>
                    <input type="submit" value="Submit">
                </form>
            """


@app.route("/tipos-de-request-4", methods=["GET", "POST"])
def tipos_de_request_4():
    metodo = request.method

    if metodo == "GET":
        return f""" El tipo de pedido fue <h1>{metodo}</h1>
                    <form action="/tipos-de-request-4" method="post">
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
