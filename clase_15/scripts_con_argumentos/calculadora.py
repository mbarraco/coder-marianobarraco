import sys

# Obtener los argumentos de línea de comandos
args = sys.argv

# Verificar que se proporcionen suficientes argumentos
if len(args) != 4:
    print(f"Cantidad de argumentos incorrecta. Proporcionaste {len(args) - 1} y necesitamos 3 argumentos \n")
    sys.exit(1)

# Obtener los argumentos individuales
operacion = args[1]
num1 = float(args[2])
num2 = float(args[3])

# Realizar la operación solicitada
if operacion == 'suma':
    resultado = num1 + num2
elif operacion == 'resta':
    resultado = num1 - num2
elif operacion == 'multiplicacion':
    resultado = num1 * num2
elif operacion == 'division':
    if num2 != 0:
        resultado = num1 / num2
    else:
        raise ValueError("No se puede dividir entre cero.")
else:
    print("Operación no válida")
    sys.exit(1)

# Imprimir el resultado
print(f"El resultado de la {operacion} es: {resultado}")
