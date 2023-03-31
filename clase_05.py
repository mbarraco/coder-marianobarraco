#
# For
#
mis_bandas = ["king crimson", 1979, "greta van fleet", "war on drugs"]
'''
para cada elemento en mis_bandas:
    imprimir(element)
'''
for elemento in mis_bandas: # "bucle" o "loop"
    print("1", elemento)
print("2", elemento)

#
# For con break
#
rivales = ["Seol", "Yoo", "Hwangbo", "Song", "Choi", "Kim", "Lee", "Hong", "Park", "Cha", "Yoon", "Choi", "Jung", "Kim", "Cho", "Myung-bo", "Jin", "Hwang", "Yoon", "Kim", "Jeong", "Lee", "Kang", "Lee", "Lee", "Kim", "Kim", "Lee", "Yi", "Yoo", "Lee", "Song", "Lee", "Kim", "Choi", "Hong", "Park", "Choi", "Ahn", "Larsson", "Lucic", "Mellberg", "Jakobsson", "Ljungberg", "Nilsson", "Mild", "Kihlberg", "Hansson", "Mjällby", "Hedman", "Nordfeldt", "Andersson", "Alexandersson", "Edman", "Jonson", "Linderoth", "Mellberg", "Nordmark", "Rosenberg", "D. Andersson", "I. Svensson", "Alvbåge", "Allbäck", "Larsson", "Ljungberg", "Lučić", "Mild", "Nilsson", "Hansson", "Åman", "Andersson", "Kihlberg", "Mellberg", "Nordmark", "Prpic", "Sundin", "Allison", "Babayaro", "Ikedia", "Kanu", "Lawal", "Okocha", "Onyewu", "Sodje", "West", "Yobo", "Adepoju", "Aghahowa", "Aloisi", "Amokachi", "Babayaro", "E. George", "J. Okocha", "O. Martins", "A. West", "T. Aghahowa", "T. Babayaro", "C. Enyeama", "I. Okoronkwo", "J. Yobo"]
clubes = ["Argentinos Juniors", "Boca Juniors", "Defensa y Justicia", "Racing Club", "River Plate", "Barcelona SC", "Independiente del Valle", "Liga Deportiva Universitaria", "Olimpia", "Cerro Porteño", "Club Guaraní", "América de Cali", "Atlético Nacional", "Junior Barranquilla"]
# Contra argentina jugó algún jugador llamdo Larson de apellido?
# para cada elemento en rivales:
#     si el elemento en minuscula es igual a "erikson" entonces imprimilo por pantalla
for rival in rivales:
    if rival.lower() == "larsson":
        print("Encontré a larsson!")
        break
print("fin: ", rival)
for rival in clubes:
    print(rival)

#
# for-else
#
rivales = ["Seol", "Yoo", "Hwangbo", "Song", "Choi", "Kim", "Lee", "Hong", "Park", "Cha", "Yoon", "Choi", "Jung", "Kim", "Cho", "Myung-bo", "Jin", "Hwang", "Yoon", "Kim", "Jeong", "Lee", "Kang", "Lee", "Lee", "Kim", "Kim", "Lee", "Yi", "Yoo", "Lee", "Song", "Lee", "Kim", "Choi", "Hong", "Park", "Choi", "Ahn", "Larsson", "Lucic", "Mellberg", "Jakobsson", "Ljungberg", "Nilsson", "Mild", "Kihlberg", "Hansson", "Mjällby", "Hedman", "Nordfeldt", "Andersson", "Alexandersson", "Edman", "Jonson", "Linderoth", "Mellberg", "Nordmark", "Rosenberg", "D. Andersson", "I. Svensson", "Alvbåge", "Allbäck", "Larsson", "Ljungberg", "Lučić", "Mild", "Nilsson", "Hansson", "Åman", "Andersson", "Kihlberg", "Mellberg", "Nordmark", "Prpic", "Sundin", "Allison", "Babayaro", "Ikedia", "Kanu", "Lawal", "Okocha", "Onyewu", "Sodje", "West", "Yobo", "Adepoju", "Aghahowa", "Aloisi", "Amokachi", "Babayaro", "E. George", "J. Okocha", "O. Martins", "A. West", "T. Aghahowa", "T. Babayaro", "C. Enyeama", "I. Okoronkwo", "J. Yobo"]
for rival in rivales:
    if rival.lower() == "larsson":
        print("encontré a Larsson")
else:
    print(f"longitud de la lista: {len(rivales)}")

#
# continue
#
rivales = ["Seol", "Yoo", "Hwangbo", "Song"]
for rival in rivales:
    if rival.lower() == "seol":
        print("no me he salteado a Seol")
    if rival.lower() == "yoo":
        print("encontré a Yoo")
    if rival.lower() == "seol":
        continue
    print(f"-> jugador evaluado {rival}")

#
# Enumerate
#
rivales = ["Seol", "Yoo", "Hwangbo", "Song"]

for rival in rivales:
    print(rival)

print("*" * 90)

for indice, rival in enumerate(rivales):
    print(indice, rival)
#
# Range
#
for numero in range(5):
    print(numero)

print("*" * 90)

for numero in range(0, 5):
    print(numero)

print("*" * 90)

for numero in range(2, 7):
    print(numero)

print("*" * 90)

for numero in range(6, 15, 8):
    print(numero)

#
# While
#

# la palabra magica es "amigo"
palabra_magica = input("Di la palabra magica: ")
'''
mientras la palabra magica no sea amigo:
    decile al usuario que es incorrecta y que ingrese otra palabra palabra_magica
'''

while palabra_magica.lower() != "amigo":
    palabra_magica = input("Palabra magica incorrecta. Ingrese la palabra magica: ")

print("La puerta se ha abierto!")

#
# Ejemplo intentos
#
# la palabra magica es "amigo"
palabra_magica = input("Di la palabra magica: ")
'''
mientras la palabra magica no sea amigo:
    decile al usuario que es incorrecta y que ingrese otra palabra palabra_magica
'''

intentos = 0
while palabra_magica.lower() != "amigo":
    if intentos > 3:
        break
    palabra_magica = input("Palabra magica incorrecta. Ingrese la palabra magica: ")
    intentos += 1

if intentos > 3:
    print("la puerta se ha cerrado por un año")
else:
    print("La puerta se ha abierto!")

# version con "else" (by esteban)
intentos = 0
while palabra_magica.lower() != "amigo":
    if intentos > 3:
        break
    palabra_magica = input("Palabra magica incorrecta. Ingrese la palabra magica: ")
    intentos += 1
else:
    print("La puerta se ha abierto!")

if intentos > 3:
    print("la puerta se ha cerrado por un año")
