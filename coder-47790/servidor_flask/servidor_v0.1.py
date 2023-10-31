from flask import Flask

app = Flask("mi_servidor")


@app.route("/")
def home():
    return "Este es mi primer servidor! Bienvenidos"


app.run(debug=True, port=8182)
