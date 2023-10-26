# pip install Flask
# FLASK_APP=app.py FLASK_ENV=development flask run

from flask import Flask, render_template_string, request  # Added 'request' here

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'


def guardar_en_base_de_datos(user, password):
    pass

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "GET":

        return render_template_string('''
            <form action="/signup" method="post">  <!-- Changed action to /signup -->
                User: <input type="text" name="user"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" value="Submit">
            </form>
        ''')
    elif request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        guardar_en_base_de_datos(user=user, password=password)


if __name__ == '__main__':
    app.run(debug=True, port=8181)
