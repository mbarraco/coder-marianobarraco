from flask import Flask


app = Flask("El servidor de Tierra Media")

@app.route("/seleccion")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Así forma el equipo seleccionado Nacional</title>
    </head>
    <body>
        <h1>Estos son los 11 jugadores titulares</h1>
        <ul>
            <li>Emiliano Martínez - Arquero</li>
            <li>Nicolas Otamendi - Defensor</li>
            <li>Nahuel Molina - Defensor</li>
            <li>Gonzalo Montiel - Defensor</li>
            <li>Lisando Martinez - Defensor</li>
            <li>Enzo Perez - Mediocampista</li>
            <li>Rodrigo De Paul - Mediocampista</li>
            <li>Alexis McAllister - Mediocampista</li>
            <li>Julián Álvarez - Delantero</li>
            <li>Ángel Di María - Delantero</li>
            <li>Lionel Messi - Delantero</li>
        </ul>
    </body>
    </html>
    """


app.run(debug=True, port=8000)
