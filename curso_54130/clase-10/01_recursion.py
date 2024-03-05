"""
Factorial: operador algebraico "!"

Ejemplos:
    1) 5! = 5 * 4 * 3 * 2 * 1
    2) 0! = 1
    3) 1! = 1
    4) 3! = 3 * 2 * 1
    5) 4! = 4 * 3 * 2 * 1 = 24

Observación
    1) 5! = 5 * 4 * 3 * 2 * 1
    2) 4! = 4 * 3 * 2 * 1
    3) 5! = 5 * 4!

"""

# Ejercicio 1

# def calcular_factorial(numero):
#     resultado = 1
#     while numero > 0:
#         resultado = resultado * numero
#         numero -= 1
#     return resultado

# def calcular_factorial(numero):
#     factorial = 1
#     for i in range(1, numero + 1):
#         factorial *= i
#     return factorial


def calcular_factorial(numero):
    """Observación
    1) 5! = 5 * 4 * 3 * 2 * 1
    2) 4! = 4 * 3 * 2 * 1
    3) 5! = 5 * 4!
    """

    print(f"Me invocaron con el valor numero = {numero}")
    if numero == 0:
        return 1
    else:
        return numero * calcular_factorial(
            numero - 1
        )  # return numero * el factorial del anterior a mi numero como hizo Thomas


print(calcular_factorial(4))
