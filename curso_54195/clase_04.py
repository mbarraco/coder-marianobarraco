
# Hasta el 'Exit'
numeros = []
no_debo_parar = True
while no_debo_parar:
    numero = input("Ingresar un número entero o la palabra 'exit': ")
    if numero.lower() == "exit":
        no_debo_parar = False
    else:
        numeros.append(int(numero))
print(sum(numeros))

# promedio
# Ingresar cantidad deseada y devolver promedio
cantidad = int(input("Ingresar cantidad deseada de números: "))
suma = 0
for _ in range(cantidad):
    numero =  float(input("Ingresar valor: "))
    suma += numero
print(suma / cantidad)

# alternativa con While
cantidad = int(input("Ingresar cantidad deseada de números: "))
i = 0
suma = 0
while i < cantidad:
    numero =  float(input("Ingresar valor: "))
    suma += numero
    i += 1
print(suma / cantidad)

# alternativa guardando valores
cantidad = int(input("Ingresar cantidad deseada de números: "))
registro = []
for _ in range(cantidad):
    numero = float(input("Ingresar valor: "))
    registro.append(numero)

print(
    sum(registro) / len(registro)
)


# Suma de impares
suma = 0
for i in range(101):
    if i % 2 != 0:
        print(i)
        suma += i
print(suma)

# ejemplo más compacto
suma = 0
for i in range(1, 101, 2):
    suma += i
print(suma)

# ejemplo más compacto aún
print(sum(range(1, 101, 2)))


# "numero correcto"
numeros_correctos = [1, 3, 5]
while True:
    numero = int(input("Ingresar número: "))
    if numero in numeros_correctos:
        print(f"El numero {numero} es correcto")
        break
    else:
        print("numero incorrecto")


# Calculadora
while True:

    operacion = input("Ingresar operacion (+, -, *, 'exit'): ")

    if operacion.lower() == "exit":
        print("Programa finalizado")
        break
    elif operacion == "+":
        #completar todas las operacion
    else:
        # completar