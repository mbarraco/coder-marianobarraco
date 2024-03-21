from flask import Flask, request, render_template_string




from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('xxx-yyy.html')



app = Flask("Mi servidor")

@app.route("/seleccion")  # Ruta (en django estaría en urls.py)
def mi_vista():
    contexto_dict = {
        'players': [
            "Emiliano Martínez - Arquero",
            "Nicolas Otamendi - Defensor",
            "Nahuel Molina - Defensor",
            "Gonzalo Montiel - Defensor",
            "Lisando Martinez - Defensor",
            "Angel di maria - Mediocampista"
        ]
    }
    rendered_template = template.render(contexto_dict)
    print(rendered_template)
    return rendered_template

app.run(debug=True, port=8000)
