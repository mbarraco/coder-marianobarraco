import requests
import sys

def get_country_info(country_name):
    url = f"https://restcountries.com/v2/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        country_data = response.json()[0]
        print("Información del país:")
        print(f"Nombre: {country_data['name']}")
        print(f"Capital: {country_data['capital']}")
        print(f"Población: {country_data['population']}")
        print(f"Área: {country_data['area']} km²")
        print(f"Región: {country_data['region']}")
    else:
        print("No se pudo obtener la información del país.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Por favor, proporcione el nombre de un país como argumento.")
    else:
        country_name = sys.argv[1]
        get_country_info(country_name)
