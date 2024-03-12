import json


mi_lista = ["Magenta", "Riff Raff", "Columbia", "Rocky", 4, 5, True]

f = open("personajes.txt", "w")
lista_convertida_a_json = json.dumps(mi_lista)
f.write(lista_convertida_a_json)

f.close()

f = open("personajes.txt", "r")
contenido = f.read()
mi_lista_leida = json.loads(contenido)
f.close()
print(mi_lista_leida)
print(type(mi_lista_leida))
