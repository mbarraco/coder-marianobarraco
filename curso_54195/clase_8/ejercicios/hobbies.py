import json

hobbies = []
while len(hobbies) < 3:

    hobby = input("ingresar hobby: ")
    hobbies.append(hobby)

print(hobbies)

nombre_de_archivo = "hobbies.json"
with open(nombre_de_archivo, "w") as outfile:
    hobbies_en_formato_texto = json.dumps(hobbies)
    outfile.write(hobbies_en_formato_texto)