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