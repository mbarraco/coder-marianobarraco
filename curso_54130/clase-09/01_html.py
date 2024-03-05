FILAS = 8
COLUMNAS = 10


def crear_tablero(posicion_fila, posicion_columna):
    tablero = []
    for i in range(FILAS):
        fila = ["."] * COLUMNAS
        tablero.append(fila)
    tablero[posicion_fila][posicion_columna] = "0"
    return tablero


def generarar_tablero_en_version_html(tablero):
    tablero_html = "<table>"
    for fila in tablero:
        tablero_html += "<tr>"
        for posicion in fila:
            if posicion == "0":
                tablero_html += f'<td style="color: red;">{posicion}</td>'
            else:
                tablero_html += f"<td>{posicion}</td>"
        tablero_html += "</tr>"
    tablero_html += "</table>"
    return tablero_html


# Assuming 'tablero' is your board matrix
tablero = crear_tablero(7, 9)
tablero_en_html = generarar_tablero_en_version_html(tablero)

style = """
    <style>
    body {
        text-align: center;
    }
    .container {
        margin: auto;
        width: 50%;
    }
    table {
        border-collapse: collapse;
        margin: auto;
    }
    td, th {
        border: 1px solid #ddd;
        text-align: center;
        padding: 8px;
    }
    tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    textarea {
        width: 80%; /* Adjust based on preference */
        margin-bottom: 20px; /* Adds some space below the textarea */
    }
    </style>
"""


texto_en_formato_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Board Game</title>
    {style}
</head>
<body>
    <!-- Visible title for the user -->
    <h1>Bienvenido a mi juego!</h1>

    <!-- Text box for instructions -->
    <textarea id="gameInstructions" name="gameInstructions" rows="5" cols="50" readonly style="resize:none;">
        Game Instructions:
        - Step 1: ...
        - Step 2: ...
        - Step 3: ...
    </textarea>

    <!-- Placeholder for the board -->
    {tablero_en_html}
</body>
</html>
"""

print(texto_en_formato_html)
