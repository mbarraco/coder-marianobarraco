"""
Un curso se ha dividido en dos grupos diferentes: A y B de acuerdo al nombre y a una preferencia
(Marvel o Capcom). El grupo A está formado por fans de Marvel con un nombre anterior a la M y los
fans de Capcom con un nombre posterior a la N y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y preferencia, y muestre por pantalla
el grupo que le corresponde.
Ej.:
    ¿Cómo te llamas?  Alan
    ¿Cuál es tu preferencia (M o C)?  C
    Tu grupo es B
    Para preguntarle al usuario, recuerda usar input.
"""

# Prueba 1
nombre_1 = "Abel"
preferencia_1 = "Marvel"
grupo_esperado_1 = "A"

# Prueba 2
nombre_2 = "Abel"
preferencia_2 = "Capcom"
grupo_esperado_2 = "B"

# Prueba 3
nombre_3 = "Sara"
preferencia_3 = "Marvel"
grupo_esperado_3 = "B"

# Prueba 4
nombre_4 = "Sara"
preferencia_4 = "Capcom"
grupo_esperado_4 = "A"


#################
# Algoritmo

nombre = nombre_4
preferencia = preferencia_4
grupo_esperado = grupo_esperado_4


if nombre.lower() < "m":
    if preferencia.lower() == "marvel":
        grupo = "A"
    else:
        grupo = "B"
else:
    if preferencia.lower() == "marvel":
        grupo = "B"
    else:
        grupo = "A"


print("grupo esperado: ", grupo_esperado)
print("grupo asignado: ", grupo)