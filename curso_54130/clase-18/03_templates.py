from flask import Flask, request, render_template_string




from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('zzz.html')



app = Flask("Mi servidor")

@app.route("/seleccion")  # Ruta (en django estaría en urls.py)
def mi_vista():
    contexto_dict = {
        'players': [
            {"nombre": "Emiliano Martínez ", "rol": "arquero"},
            {"nombre": "Nicolas Otamendi ", "rol": "defensor"},
            {"nombre": "Nahuel Molina ", "rol": "defensor"},
            {"nombre": "Gonzalo Montiel ", "rol": "defensor"},
            {"nombre": "Lisando Martinez ", "rol": "defensor"},
            {"nombre": "Angel di maria", "rol": "mediocampista"},
            {"nombre": "Julián Álvarez", "rol": "delantero"},
        ]
    }
    rendered_template = template.render(contexto_dict)
    print(rendered_template)
    return rendered_template

app.run(debug=True, port=8000)
