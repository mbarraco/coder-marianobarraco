import requests
import json


direccion =  "http://restcountries.com/v3.1/all"

respuesta = requests.get(direccion)

print(respuesta.status_code)
print(type(respuesta.json()))

paises_sin_procesar = respuesta.json()

for i, pais_sin_procesar in enumerate(paises_sin_procesar):
    # print(i, type(pais_sin_procesar))
    # print(i, pais_sin_procesar.keys())
    print(i, pais_sin_procesar["name"]["official"])



mi_archivo = open("paises.json", "w")

json.dump(paises_sin_procesar, mi_archivo)

