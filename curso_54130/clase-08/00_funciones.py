def func_1():
    print("hola!")


def func_2(palabra):
    print(f"hola, {palabra}!")


def func_3(palabra, numero):
    print(f"hola, {palabra}! son las {numero} de la tarde")


def func_4(numero):
    numero += 1
    print(f"numero: {numero}")


def func_5(numero):
    numero += 1
    print(f"numero: {numero}")
    # devolver numero al exterior
    return numero


def func_6(fila, columna):
    fila += 1
    columna += 1
    return fila, columna


# func_1()
# func_2("Esteban")
# func_3("Esteban", 8)

fila = 0
func_4(fila)
print(f"fila: {fila}")

print()

fila = 0
fila = func_5(fila)
print(f"fila: {fila}")

print()

fila = 0
columna = 0
fila, columna = func_6(fila, columna)
print(f"6 --> fila: {fila}")
print(f"6 --> columna: {columna}")
