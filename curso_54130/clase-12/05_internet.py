import requests


while True:
    print()
    pais = input("Ingrese el pais que quiere: ")
    direccion_web = f"https://restcountries.com/v3.1/name/{pais}"
    pedido_web = requests.get(direccion_web)
    informacion = pedido_web.json()

    informacion_en_diccionario = informacion[0]
    latitud_longitud = informacion_en_diccionario["latlng"]
    paises_fronterizos = informacion_en_diccionario["borders"]
    nombre = informacion_en_diccionario["name"]["common"]
    capital = informacion_en_diccionario["capital"]
    print(nombre, latitud_longitud, paises_fronterizos, capital)
