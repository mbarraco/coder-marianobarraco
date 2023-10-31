import json


mi_diccionario = {
    1: True,
    "2": None,
    "3": "three",
}
print(mi_diccionario)
print(mi_diccionario["3"])
print("_" * 90)

mi_archivo = open("mi_archivo.json", "w")
json.dump(mi_diccionario, mi_archivo)
mi_archivo.close()
