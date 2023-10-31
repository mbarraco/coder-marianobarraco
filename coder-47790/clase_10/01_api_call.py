import requests


def consultar_capital(pais="argentina"):
    direccion = f"https://restcountries.com/v3.1/name/{pais}"

    respuesta = requests.get(direccion)
    informacion = respuesta.json()

    # print(type(informacion))
    # print(len(informacion))
    data = informacion[0]
    # print(type(data))

    # for clave in data:
    #     print(clave)

    capital = data["capital"]
    subregion = data["subregion"]

    print(capital, subregion)


consultar_capital("argentina")
consultar_capital("bolivia")
consultar_capital("namibia")
consultar_capital()
