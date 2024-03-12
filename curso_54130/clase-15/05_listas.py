mi_lista = ["Magenta", "Riff Raff", "Columbia", "Rocky", 4, 5, True]

f = open("personajes.txt", "w")
f.write(str(mi_lista))
f.close()

f = open("personajes.txt", "r")
contenido = f.read()
f.close()
print(contenido)
print(list(contenido))
print(type(contenido))
