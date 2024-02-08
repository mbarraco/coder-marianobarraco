import time
# 1. Imprimir por pantalla los valores de las variables xx e yy.

# xx = 0
# yy = 10
# print(f"La variable xx vale: {xx}")
# print(f"La variable yy vale: {yy}")

# 2. Imprimir por pantalla los valores de las variables xx e yy 10 veces cada uno.

# xx = 0
# yy = 10

# Kenneth
# print(str(xx)*10, str(yy)*10)
# print()

# Mariano
# print([xx] * 10)
# print([yy] * 10)
# print()

# Luciano
# xx = 0
# yy = 10
# for i in range(10):
#     time.sleep(1)
#     print(f"La variable 'i' vale: {i}")
#     print(f"La variable xx vale: {xx}")
#     print(f"La variable yy vale: {yy}")
#     print()

# 3. Modificar el ejercio anterior para que el valor de xx aumente hasta 9
# y el valor de yy disminuya hasta 1

xx = 0
yy = 10

# Kenneth
# for i in range(10):
#     time.sleep(i)
#     print(f"El valor de xx es: {xx}")
#     xx += 1
#     print(f"El valor de yy es {yy}")
#     yy -= 1
#     print()

# # Emmanuel
# for i in range(9):
#     time.sleep(.5)
#     xx = xx + 1
#     yy = yy - 1
#     print(xx, yy)
#     print()

# # Maria Silvina
xx = 0
yy = 10
for i in range(10):
    time.sleep(1)
    print(f"La variable 'i' vale: {i}")
    print(f"La variable xx vale: {xx + i}")
    print(f"La variable yy vale: {yy - i}")
    print()