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