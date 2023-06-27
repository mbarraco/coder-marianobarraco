# Un año es bisiesto si:
# 1. Es divisible por 4 y NO ES divisible por 100, ej: 96, 1096
# 2. O, es divisble por 400: ej: 2000, 2400

# Escribir un programa que pida al usuario ingresar un año y
# nos diga por pantalla si es bisiesto o no.

year = int(input("Ingresar un año: "))

# version 1
if year % 400 == 0:
    print(f"1. El año {year} es bisiesto!")
elif year % 4 == 0 and year % 100 != 0:
    print(f"1. El año {year} es bisiesto!")
else:
    print(f"1. El año {year} NO es bisiesto!")

# version 2
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"2. El año {year} es bisiesto!")
else:
    print(f"2. El año {year} NO es bisiesto!")

# version 3
condicion_1 = (year % 400 == 0)
condicion_2 = (year % 4 == 0 and year % 100 != 0)

if condicion_1 or condicion_2:
    print(f"3. El año {year} es bisiesto!")
else:
    print(f"3. El año {year} NO es bisiesto!")

# version 4

default_msg = f"4. el número {year} no es bisiesto"

if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
    default_msg = f"4. el número {year} es bisiesto"

print(default_msg)

# REGRESAMOS  21:43 HORA ARGENTINA

# A partir de dos variables llamadas NOMBRE y EDAD (deben ser datos solicitados al usuario con input),
# debes crear una variable de tipo bool cuyo valor sea True si se cumplen
# TODAS las siguientes condiciones, encadenando operadores lógicos en una sola línea:

# * NOMBRE sea diferente de cuatro asteriscos “****”
# * EDAD sea mayor que 5 y a su vez menor que 20
# * Que la longitud de NOMBRE sea mayor o igual a 4  pero a la vez menor que 8
# * EDAD multiplicada por 3 sea mayor que 35

# Luego muestra el resultado.
# Si te animas, puedes mostrar, en lugar del resultado booleano,
# un mensaje que indique si se cumplen o no las condiciones

age = int(input("Ingresar edad: "))
name = input("ingresar nombre: ")

condition = (name != "****") and (5 < age < 20) and (4 < len(name) < 8) and (age * 3 > 35)
print(condition)
# Casos de prueba
    # nombre = ****, edad = 8 -> False
    # nombre = * edad = 4 -> False
    # nombre = * edad = 21 -> False
    # nombre = ermenegilda edad = 10 -> False
    # nombre = teo edad = 10 -> False
    # nombre = micaela edad = 6 -> False
    # nombre = micaela edad = 19 -> True