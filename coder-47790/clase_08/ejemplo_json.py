import json

mi_departamento = {
    "departamento": 8,
    "activo": True,
    "deudas": None,
    "nombre": "Ventas",
    "director": "Juan Rodríguez",
    "empleados": [
        {"nombre": "Pedro", "apellido": "Fernández"},
        {"nombre": "Jacinto", "apellido": "Benavente"},
    ],
}

mi_archivo = open("departamento.json", "w")

json.dump(mi_departamento, mi_archivo)

mi_archivo.close()


# Leer el archivo de dos maneras distintas

mi_archivo_de_lectura_1 = open("departamento.json", "r")
contenido_1 = mi_archivo_de_lectura_1.read()

mi_archivo_de_lectura_2 = open("departamento.json", "r")
contenido_2 = json.load(mi_archivo_de_lectura_2)


print(type(contenido_1))
print(contenido_1["director"])

print(type(contenido_2))
print(contenido_2["director"])
