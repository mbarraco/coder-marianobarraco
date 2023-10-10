from pprint import pprint as pp


mi_diccionario = {}
mi_diccionario = dict()

print(mi_diccionario)

mi_diccionario["clave_01"] = "valor_01"
mi_diccionario["clave_02"] = 5000
mi_diccionario["alejandro"] = [1, 2, 100]
mi_diccionario["nombre"] = "mariano"
mi_diccionario[45] = "spain"
mi_diccionario[(1,2,3)] = "argentina"

pp(mi_diccionario)

respuesta = "mariano" in mi_diccionario
print(respuesta)

respuesta = "mariano" in mi_diccionario.keys()
print(respuesta)

respuesta = "mariano" in mi_diccionario.values()
print(respuesta)

mi_diccionario[45] = "12312319fphauewrghpfeiurhg"


pp(mi_diccionario)

mi_otro_diccionario = {
    1: "uno",
    2: "dos",
    3: "tres",
}
pp(mi_otro_diccionario)
mi_diccionario.update(mi_otro_diccionario)
pp(mi_diccionario)