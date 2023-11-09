from flask import Flask, request  # Added 'request' here
from datetime import datetime


from juego_web import Juego


app = Flask("mi_servidor")

juego = Juego()

@app.route("/ping", methods=["GET", "POST"])
def segundos():
    segundos = round(datetime.now().timestamp(), 1)
    return f"[{segundos}] - recibí un request del tipo: {request.method}"



@app.route("/form-1")
def form_1():
    metodo = request.method
    return f""" El tipo de pedido fue <h1>{metodo}</h1>
                <form action="/ping" method="POST">
                    <input type="submit" value="Submit">
                </form>
            """


@app.route("/partida-sin-css", methods=["GET", "POST"])
def partida_sin_css():
    metodo = request.method


    form_control_de_jugador = f"""
            <!DOCTYPE html>
            <html lang="es">
            <head>
            <meta charset="UTF-8">
            <title>Juego de Tablero</title>
            </head>
            <body>

            <h2>Control de Movimientos del Jugador</h2>

            <!-- Contenedor para el tablero -->
            <div id="tablero">
            <!-- El tablero actualizado se mostrará aquí -->
            </div>

            <!-- Formularios para los movimientos -->
            <form action="partida-sin-css" method="post">
            <input type="hidden" name="movimiento" value="w">
            <button type="submit">Arriba (W)</button>
            </form>

            <form action="partida-sin-css" method="post">
            <input type="hidden" name="movimiento" value="a">
            <button type="submit">Izquierda (A)</button>
            </form>

            <form action="partida-sin-css" method="post">
            <input type="hidden" name="movimiento" value="s">
            <button type="submit">Abajo (S)</button>
            </form>

            <form action="partida-sin-css" method="post">
            <input type="hidden" name="movimiento" value="d">
            <button type="submit">Derecha (D)</button>
            </form>

            </body>
            </html>


            """

    if metodo == "GET":
        return form_control_de_jugador
    else:
        # user = request.form.get("user")
        # password = request.form.get("password")

        return form_control_de_jugador


@app.route("/partida", methods=["GET", "POST"])
def partida():

    with open("juego.html", "r") as f:
        form_control_de_jugador = f.read()


    if request.method == "GET":
        tablero = juego.obtener_tablero_actual()
        tablero =  f'<div class="tablero"> {tablero} </div>'
        pantalla_para_el_jugador = tablero + form_control_de_jugador
        return pantalla_para_el_jugador
    else:
        jugada = request.form.get("jugada")
        print(jugada)
        juego.registrar_jugada(jugada)

        tablero = juego.obtener_tablero_actual()
        tablero =  f'<div class="tablero"> {tablero} </div>'
        pantalla_para_el_jugador = tablero + form_control_de_jugador

        return pantalla_para_el_jugador



app.run(debug=True, port=8182)



