# 1. Escribir un programa que imprima por pantalla una "columna" hecha de 10 puntos "."

# for punto in range(10):
#     print(".")

# 2. Modificar el ejercicio anterior para que dibuje una columna de 9 puntos y un "0".
#    El "0" no puede estar ni al comienzo ni al final de la columna
# Emmanuel
# for index in range(10):
#     if index == 1:
#         print(0)
#     else:
#         print(".")


# 3. Modificar el ejercicio anterior para que sea el usuario el que decida en dónde imprimir el "0"

# numero = int(input("Elija la posición en la que quiera poner el 0: "))

# if numero > 10 or numero < 0:
#     print("error")
# else:
#     for i in range(10):
#         if i == numero - 1:
#             print("0")
#         else:
#             print(".")

# 4. Escribir un código que genere 10 filas de 10 "."
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........

# for i in range(10):
#     print("." * 10)


# 5. Modificar el ejercicio anterior para que aparezca un "0" en la posición (4,1)

# fila_limpia = ["." ]* 10
# for e in range(10):
#   if e == 4:
#     print ([".", "0", ".", ".",".", ".",".", ".",".", ".",])
#   else:
#     print(fila_limpia)

# fila_limpia = ["."] * 10
# for e in range(10):
#   if e == 4:
#     fila = fila_limpia.copy() # copy() se usa para copiar y que no se sobreescriba `fila_limpia`
#     fila[1] = "0"
#     # fila es igual al copy de fila limpia y fila limpia queda igual
#     # El join esta convirtiendo la lista en string y separándolo con los espacios
#     print(" ".join(fila))
#   else:
#     print(" ".join(fila_limpia))

# 5. Modificar el ejercicio anterior para que el usuario decida dónde dibujar el circulo en mi tablero


# posicion_fila = int(input("Elija la fila en la que quiera poner el 0: "))
# posicion_columna = int(input("Elija la columna en la que quiera poner el 0: "))
# decision_de_usuario = input("Elegir caracter de reprentacion de casillero en el tablero: ")

# fila_limpia = [decision_de_usuario] * 10
# for e in range(10):
#   if e == posicion_fila:
#     fila = fila_limpia.copy() # copy() se usa para copiar y que no se sobreescriba `fila_limpia`
#     fila[posicion_columna] = "0"
#     # fila es igual al copy de fila limpia y fila limpia queda igual
#     # El join esta convirtiendo la lista en string y separándolo con los espacios
#     print(" ".join(fila))
#   else:
#     print(" ".join(fila_limpia))


