aviones = {"bombardero": "b17", "caza": "yak-1", "transporte": "DC-3"}

print("ataque" in aviones.keys())
print(aviones.keys())
print()
print("il-2" in aviones.values())
print(aviones.values())


print()
print()
# para cada clave en el diccionario aviones: imprimi cada clave
for cada_clave in aviones.keys():
    print(cada_clave)
print()
for cada_valor in aviones.values():
    print(cada_valor)

print()
for zz in aviones.values():
    print(zz)

print()
for xx, yy in aviones.items():
    print(f"El avion {yy} es de tipo {xx}")

print()
