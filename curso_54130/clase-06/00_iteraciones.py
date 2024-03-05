# Una Prueba está aprobada si la calificación excede a 5.
# Las calificaciones van entre 0 y 10
# Consigna: para cada calificación en `lista_de_calificaciones` imprimir
# "Prueba aprobada" o "Prueba fallida" según corresponda
#
# Ejemplo:
# lista_de_calificaciones = [5, 0, 9]
#
# Salida por consola:
# >> Prueba Fallida
# >> Prueba Fallida
# >> Prueba Superada

# Recordemos


def imprimir_aprobado():
    print("Prueba aprobada")


lista_de_calificaciones = [1, 2, 10, 4]

# para cada elemento en lista_de_calificaciones: imprimirlo por pantalla
for calificacion in lista_de_calificaciones:
    esta_aprobado = calificacion > 5
    # print(f"La calificacion es aprobada: {esta_aprobado}")

    print(f"La calificación es: {calificacion}")
    # SI esta_aprobado es verdadero (True):
    if esta_aprobado == True:
        imprimir_aprobado()
    # de otra forma:
    else:
        print("Prueba fallida")
    print()
