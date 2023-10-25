import json


mi_archivo = open("mi_archivo.json", "r")
xx = mi_archivo.read()
mi_archivo.close()
print(xx)
print(type(xx))

print("\n")

# Forma numero 1
mi_archivo = open("mi_archivo.json", "r")
xx = json.load(mi_archivo)
mi_archivo.close()
print(type(xx))
print(xx["3"])

print("\n")

# Forma numero 2 (repito codigo de arriba)
mi_archivo = open("mi_archivo.json", "r")
xx = mi_archivo.read()
mi_archivo.close()
print(xx)
print(type(xx))


print("\n")

xx = json.loads(xx)
print(xx)
print(type(xx))
