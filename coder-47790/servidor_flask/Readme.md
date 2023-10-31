
# Sevidor HTTTP: Flask

## 1. Instalar Python + PIP
Necesitaremos Python y PIP, que es una herraamienta para instalar biliotecas no provistas con la instalación de Python.

Este tutorial explica como instalarlo en
1. windows: https://www.youtube.com/watch?v=GLcbD-mCAO8&ab_channel=solvetic.com
2. Mac: https://www.youtube.com/watch?v=pEXPvVK13Lo&ab_channel=solvetic.com


## 2. Instalar Flask

En la terminal ejecutar: `pip install flask`


## 3. Servidor

### Versión 0.1
Las siguientes 6 líneas de código componen la primer versión de nuestro servidor.
```python
from flask import Flask


app = Flask("mi_servidor")

@app.route('/')
def home():
    return 'Este es mi primer servidor! Bienvenidos'

app.run(debug=True, port=8182)
```
para ejecutar el servidor en esta primer versión:
```bash
>> python servidor_v0.1.py
```
lo cual debería mostrarnos en la terminal:
```bash
 * Serving Flask app 'mi_servidor'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8182
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 115-862-265
127.0.0.1 - - [31/Oct/2023 08:23:45] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [31/Oct/2023 08:23:45] "GET /favicon.ico HTTP/1.1" 404 -
```

si todo esto se cumple, podremos realizar pedidos, *requests*, a nuestro servidor desde cualquier navegador (e.g. Chrome) mediante esta dirección
[http://127.0.0.1:8182/](http://127.0.0.1:8182/)


### Version 0.2

Presentamos `HTML`: una forma de procesar el texto y hacer que los navegadores lo "dibujen mejor"

```python
from flask import Flask

app = Flask("mi_servidor")


@app.route("/")
def home():
    return """
            <div class="welcome-container">
                <h1>Welcome to Our Page!</h1>
                <p>This is a simple welcome message for beginner students learning HTML.</p>
            </div>
        """

app.run(debug=True, port=8182)
```
### Versión 0.3

Presentamos más posibilidades de control de estilos con `HTML`

```python
from flask import Flask, render_template_string, request  # Added 'request' here
from datetime import datetime
import json

app = Flask("mi_servidor")

@app.route('/')
def home():
    return """
                    <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Welcome Message</title>
            <style>
                /* Basic styling for centered content and font */
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f5f5f5;
                }
                .welcome-container {
                    background-color: #ffffff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                }
            </style>
        </head>
        <body>
            <div class="welcome-container">
                <h1>Welcome to Our Page!</h1>
                <p>This is a simple welcome message for beginner students learning HTML.</p>
            </div>
        </body>
        </html>

        """

app.run(debug=True, port=8182)

```
### Version 0.4

Agregamos una nueva `route` o `URL`

```python
from flask import Flask
from datetime import datetime
app = Flask("mi_servidor")


@app.route("/")
def home():
    return """
                    <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Welcome Message</title>
            <style>
                /* Basic styling for centered content and font */
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f5f5f5;
                }
                .welcome-container {
                    background-color: #ffffff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                }
            </style>
        </head>
        <body>
            <div class="welcome-container">
                <h1>Welcome to Our Page!</h1>
                <p>This is a simple welcome message for beginner students learning HTML.</p>
            </div>
        </body>
        </html>

        """


@app.route('/segundos')
def segundos():
    segundos = round(datetime.now().timestamp(), 1)
    return f'Hola!  desde el 1 de Enero de 1970 hasta este momento, pasaron: {segundos} segundos'

app.run(debug=True, port=8182)
```

### Versión 0.5

En esta versión incluimos 2 cambios:
1. El contendio `html` lo *servimos* desde un archivo en vez de hacerlo desde el código del servidor. El archivo se llama `home.html`
2. Creamos una nueva ruta `/error` para mostrar cómo veríamos un error en nuestro servidor y poder aprender a leerlo

```python
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


@app.route('/segundos')
def segundos():
    segundos = round(datetime.now().timestamp(), 1)
    return f'Hola!  desde el 1 de Enero de 1970 hasta este momento, pasaron: {segundos} segundos'

app.run(debug=True, port=8182)
```

### Versión 0.6

En esta versión comenzamos a explorar los "Tipos de pedido o `request`"

```python
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
    tipo_de_pedido = request.method
    return f"Hola! el tipo de pedido fue: {tipo_de_pedido}"


app.run(debug=True, port=8182)
```


### Versión 0.7

En esta versión comenzamos a hacer que la respuesta de nuestro servidor dependa del tipo de request, no sólo de la ruta.

```python
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

    return f""" El tipo de pedido fue {metodo}
                <form action="/tipos-de-request-2" method="post">
                    User: <input type="text" name="user"><br>
                    Password: <input type="password" name="password"><br>
                    <input type="submit" value="Submit">
                </form>
            """


@app.route("/tipos-de-request-3", methods=["GET", "POST"])
def tipos_de_request_3():
    metodo = request.method

    return f""" El tipo de pedido fue {metodo}
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
        return f""" El tipo de pedido fue {metodo}
                    <form action="/tipos-de-request-4" method="post">
                        User: <input type="text" name="user"><br>
                        Password: <input type="password" name="password"><br>
                        <input type="submit" value="Submit">
                    </form>
                """
    else:
        user = request.form.get("user")
        password = request.form.get("password")

        return f""" El tipo de pedido fue {metodo}. <br>
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

```