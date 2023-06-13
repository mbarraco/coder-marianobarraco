
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
# Ejemplo en vivo 1
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

###############################################################################
# Ejemplo en vivo 2
###############################################################################
mi_conjunto = {"Rojo", "Blanco", "Azul"}
print(mi_conjunto)
mi_conjunto.add("Violeta")
mi_conjunto.add("Dorado")
mi_conjunto.remove("Dorado")
mi_conjunto.remove("Blanco")
mi_conjunto.discard("Celeste")
print(mi_conjunto)
# mi_conjunto.remove("Celeste")  No se puede hacer porque "Celeste" no pertenece al mi_conjunto

###############################################################################
# Ejemplo en vivo 3
###############################################################################
# texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
from pprint import pprint
texto =  ("gordon lanzó su curva&strawberry ha fall"
          "ado por un pie! -gritó Joe Castiglione&dos pie"
          "s -le corrigió Troop&strawberry menea la cab"
          "eza como disgustado… -agrega el comentarista")

print("_" * 90)
print(texto)
print("_" * 90)

lineas = texto.split("&")
pprint(lineas)
print("_" * 90)
print("." * 90)

print(lineas[0].capitalize() + "...")
print("- " + lineas[1].capitalize() + ".")
print("- " + lineas[2].capitalize() + ".")
print("- " + lineas[3].capitalize() + ".")
# print(f"- {lineas[3].capitalize()}.")
print("." * 90)
print("_" * 90)


###############################################################################
# Ejemplo en vivo 4
###############################################################################
xx = set([1,2,3])
yy = set([3,4,5])
zz = xx.difference(yy)
print(zz)


###############################################################################
# Ejemplo en vivo 5
###############################################################################
mis_divisas = {'Dolar':'$','Euro':'€', 'Libra':'£'}
divisa_solicitada = input("Ingresar divisa: ")
simbolo = mis_divisas.get(divisa_solicitada.capitalize(), "Divisa no soportada")
print(simbolo)
# print(mis_divisas[divisa_solicitada]) # no sirve para monedas que no estén el diccionario!!

###############################################################################
# Ejemplo en vivo 6
###############################################################################
nombre = input("Ingresar nombre: ")
edad = int(input("Ingresar edad: "))
direccion = input("Ingresar direccion: ")
datos_del_usuario = {
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
}
print(datos_del_usuario)