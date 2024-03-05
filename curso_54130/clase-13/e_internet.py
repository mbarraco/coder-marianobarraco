# pip install flask

from flask import Flask, request

app = Flask("Mi servidor")


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/hola", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form.get("name", "World")
        return f"Hello, {name}!"
    else:
        name = request.args.get("name", "World")
        return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True)
