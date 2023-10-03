# # Ejemplo 1
# xx = 1

# if xx > 2:
#     print("*********** 1.")
#     print(f"La variable 'xx' es mayor que 2,  pues su valor es {xx}")

# if xx > 10:
#     print("*********** 2.")
#     print(f"La variable 'xx' es mayor que 10,  pues su valor es {xx}")
# else:
#     print("*********** 3.")
#     print(f"La variable 'xx' es menor que 10")

# print("Fin del programa.")


# Ejemplo 2
# consigna: quisiera darle un premio a las personas que elijan un numero par mayor que 55
# ww = 54
# es_par = ww % 2 == 0

# if es_par:
#     print(" ---->  1")
#     if ww > 55:
#         print(" ---->  3")
#         print(f"Ganaste un premio! Has elegido {ww}")
#     else:
#         print(" ---->  4")
#         print(f"Lamentablemente no hay premio para tí. Has elegido: {ww}")
# else:
#     print(" ---->  2")
#     print(f"Lamentablemente no hay premio para tí. Has elegido: {ww}")


# # Ejemplo 3: "refactor"
# ww = 56
# es_par = ww % 2 == 0
# es_mayor_a_55 = ww > 55

# if es_par and es_mayor_a_55:
#     print(" ---->  1")
#     print(f"Ganaste un premio! Has elegido {ww}")
# else:
#     print(" ---->  2")
#     print(f"Lamentablemente no hay premio para tí. Has elegido: {ww}")

ww = "9"

if ww == 10 or ww == "diez":
    print("Es el Diez!")

if ww == 10 or ww.lower() == "diez": # Este código tiene un error de diseño
    print("Es el Diez (aunque no exactamente quizá)")