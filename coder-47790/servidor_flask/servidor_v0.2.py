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
