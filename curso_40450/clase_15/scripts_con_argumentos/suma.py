import sys

# Obtener los argumentos de línea de comandos
args = sys.argv

# Verificar que se proporcionen suficientes argumentos
if len(args) != 3:
    print(f"Cantidad de argumentos incorrecta. Proporcionaste {len(args) - 1} y necesitamos 2 argumentos \n")
    sys.exit(1)

# Obtener los argumentos individuales
num1 = float(args[1])
num2 = float(args[2])

# Realizar la operación de suma
resultado = num1 + num2

# Imprimir el resultado
print(f"El resultado de la suma es: {resultado}")
