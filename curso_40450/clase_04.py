mi_numero = 991

es_par = mi_numero % 2
print(f"Si el siguiente valor es '1' entonces {mi_numero} es impar, si es '0' entonces es par: el valor es {es_par}")

print("_________________________________________________________________________________________________")

el_resto = mi_numero % 2
es_impar = (el_resto == 1)

print(es_impar)

# Idea:
# si es_impar es verdadero: print("El numero es impar")
# en otro caso: print("El numero es par")
if es_impar is True:
    print("El numero es impar")
else:
    print("El numero es par")

#
# Ejemplo con input()
#
el_numero_del_usuario = int(input("ingrese un numero entero y presione ENTER: "))
es_par = (el_numero_del_usuario % 2 == 0)
if es_par is True:
    print(f"El numero que ingresaste ({el_numero_del_usuario}) es PAR")
else:
    print("El numero que ingresaste es IMPAR")

#
#
# En una entidad financiera, hay una regla que dice que se otorgarán créditos
# a las personas que cumplan las siguientes condiciones
#
# 1. Tienen que ser mayores que 18 años
# 2. El ingreso mensual tiene que se como mínimo 200

edad = int(input("Ingresar la edad en años: "))
ingreso_mensual = int(input("Ingresar el ingreso mensual: "))

if edad > 18 and ingreso_mensual >= 200:
    print("Credito aprobado")
else:
    print("Credito no aprobado")

# En una entidad financiera, hay una regla que dice que se otorgarán créditos
# a las personas que cumplan las siguientes condiciones
#
# 1. Tienen que ser mayores que 18 años
# 2. El ingreso mensual tiene que se como mínimo 200
# 3. Si son clientes entonces el ingreso mensual tiene que ser superior a 150

edad = int(input("Ingresar la edad en años: "))
ingreso_mensual = int(input("Ingresar el ingreso mensual: "))
es_cliente = int(input("Ingresar el '1' si es cliente o '0' si no: "))

if edad > 18:
    if es_cliente == 1:
        if ingreso_mensual > 150:
            print("(1.1) Credito aprobado")
        else:
            print("(1.2) Credito no aprobado")
    else:
        if ingreso_mensual > 200:
            print("(1.3) Credito aprobado")
        else:
            print("(1.4) Credito no aprobado")
else:
    print("(2) Credito no aprobado")

# TAREA:
# 4. Si tiene menos de 80 años entonces le ofrecemos 24 cuotas y si no le ofrecemos 12
# 5. Si el cliente tiene menos de 18 años no hacer más preguntas y denegar el crédito


#
# Elif
#
# 1. Quiero otorgar becas a los alumnos mayores a 40 años con promedio mayor que 5
# 2. Si el alumno/a tiene menos de 40 años, darle la beca si su promedio es 10
edad = int(input("Ingresar la edad en años: "))
promedio = float(input("Ingresar el promedio: "))
if edad > 40:
    if promedio > 5:
        print("1.1 Otorgar beca!")
    else:
        print("1.2 No otorgar beca")
elif promedio == 10:
    print("2.1 Otorgar beca")
else:
    print("3.1 No otorgar beca")

# Ejercicio
'''
Un curso se ha dividido en dos grupos diferentes: A y B de acuerdo al nombre y a una
preferencia (Marvel o Capcom). El grupo A está formado por fans de Marvel con un nombre
anterior a la M y los fans de Capcom con un nombre posterior a la N y el grupo B por el resto.

Escribir un programa que pregunte al usuario su nombre y preferencia, y muestre por pantalla el
grupo que le corresponde.
Ej.:
¿Cómo te llamas?  Alan
¿Cuál es tu preferencia (M o C)?  C
Tu grupo es B
Para preguntarle al usuario, recuerda usar input.

'''
preferencia = input("Ingresar preferencia: ")
nombre = input("Ingresar nombre: ")

if preferencia.lower() == "marvel":
    if nombre.lower() < "m":
        print("-> 1")
        grupo = "A"
    else:
        print("-> 2")
        grupo = "B"
elif preferencia.lower() == "capcom":
    if nombre.lower() > "n":
        print("-> 3")
        grupo = "A"
    else:
        print("-> 4")
        grupo = "B"
else:
    grupo = "invalido"
    print(f"PREFERNCIA INVALIDA: {preferencia}")

print(f"El usuario '{nombre}' pertenece al grupo '{grupo}'")