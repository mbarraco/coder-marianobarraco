def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


suma_1 = sumar(2, 5)
suma_2 = sumar(5, 2)
son_iguales = suma_1 == suma_2
print("1 --> ", f"suma_1 y suma_2 son iguales: {son_iguales}")


resta_1 = restar(2, 5)
resta_2 = restar(5, 2)
son_iguales = resta_1 == resta_2
print("2 -->", f"resta_1 y resta_2 son iguales: {son_iguales}")


resta_3 = restar(a=2, b=5)
resta_4 = restar(b=5, a=2)
son_iguales = resta_3 == resta_4
print("3 -->", f"resta_3 y resta_4 son iguales: {son_iguales}")
