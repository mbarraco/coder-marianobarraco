import time

# i = 0
# # mientras i sea mayor que 4 imprimir el valor de i
# while i > 4:
#     print(i)

# j = 0
# # mientras j sea menor que 4 imprimir el valor de j
# while j < 4:
#     time.sleep(1)
#     print(j)
#     print()
#     j += 1 # equivale a `j = j + 1``


# 2. Modificar el ejercicio anterior para que:
#   a. j nunca sea mayor que 4.
#   b. j asuma los valores 0, 1, 2, y 3 infinitas veces
import time

j = 0
while j < 4:
    time.sleep(1)
    print(f"j vale: {j}")
    j += 1
    # si j es 4 entonces transormalo en 0
    if j == 4:
        j = 0
