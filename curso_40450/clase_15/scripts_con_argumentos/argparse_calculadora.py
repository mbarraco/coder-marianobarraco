import argparse

# Crear el objeto ArgumentParser
parser = argparse.ArgumentParser(description='Calculadora')

# Agregar argumentos
parser.add_argument('operacion', choices=['suma', 'resta', 'multiplicacion', 'division'], help='Operación a realizar')
parser.add_argument('num1', type=float, help='Primer número')
parser.add_argument('num2', type=float, help='Segundo número')

# Analizar los argumentos
args = parser.parse_args()

# Realizar la operación solicitada
if args.operacion == 'suma':
    resultado = args.num1 + args.num2
elif args.operacion == 'resta':
    resultado = args.num1 - args.num2
elif args.operacion == 'multiplicacion':
    resultado = args.num1 * args.num2
elif args.operacion == 'division':
    if args.num2 != 0:
        resultado = args.num1 / args.num2
    else:
        raise ValueError("No se puede dividir entre cero.")

# Imprimir el resultado
print(f"El resultado de la {args.operacion} es: {resultado}")
