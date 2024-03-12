import json


mi_lista = {
    "Magenta": 23,
    "Riff Raff": 120,
    "Columbia": 900,
    "Rocky": 0,
    4: "four",
    5: "five",
    True: True
}

f = open("personajes_dict.txt", "w")
lista_convertida_a_json = json.dumps(mi_lista)
f.write(lista_convertida_a_json)

f.close()

f = open("personajes_dict.txt", "r")
contenido = f.read()
mi_lista_leida = json.loads(contenido)
f.close()
print(mi_lista_leida)
print(type(mi_lista_leida))
