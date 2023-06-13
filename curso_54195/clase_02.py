
# Repaso conjuntos
# CRUD: crear, leer, actualizar, borrar

mi_conjunto = {1, 2, 3, "palabra", "un texto"}

mi_otro_conjunto = set(["rojo", "amarillo", "ultravioleta"])

print(mi_conjunto)

mi_conjunto.add(99)
mi_conjunto.remove("palabra")

print(mi_conjunto)


# Repaso diccionarios
from pprint import pprint
mi_diccionario = {
    "mi_clave": 1,
    "mi_otra_clave": [1, 2, 3],
    "mi_otra_clave_2": [1, 2, 3],
    "mi_otra_clave_3": [1, 2, 3],
    "mi_otra_clave_4": [1, 2, 3],
    1: "palabras",
    2: "palabras",
}
pprint(mi_diccionario)


###############################################################################
# Microdesafio 1
###############################################################################
from pprint import pprint

campeones = {
    1990: "Alemania",
    1994: "Brasil",
    1998: "Francia",
    2002: "Brasil",
    2006: "Italia",
    2010: "España",
    2014: "Alemania",
    2018: "Francia"
}

pprint(campeones)

# campeones[2022] = "Argentina" # dos opciones
campeones.update({2022: "Argentina"})
pprint(campeones)