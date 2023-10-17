import requests

direccion =  "http://restcountries.com/v3.1/all"

respuesta = requests.get(direccion)

print(respuesta.status_code)
# print(respuesta.text)
print(respuesta.json())
