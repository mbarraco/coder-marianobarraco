# Fibonacci
# posicion:                 1, 2, 3, 4, 5, 6,  7,  8, ...
# valor de Fibonacci:       1, 1, 2, 3, 5, 8, 13, 21, ...
def calcular_fibonacci(posicion):
    print(f"hola me estoy ejecutando! {posicion}")
    if posicion == 1:
        return 1
    elif posicion == 2:
        return 1
    else:
        return calcular_fibonacci(posicion - 1) + calcular_fibonacci(posicion - 2)

print(calcular_fibonacci(10))


# 1
# Escribe una función que reciba una lista por parámetro y devuelva su media

# Marcos
lista = [9, 1]
def calcular_media_1(lista):
    suma = 0
    for numero in lista:
        suma += numero
    media = suma / len(lista)
    return media

print(calcular_media_1(lista))

# Carlos
def calcular_media_2(lista):
    return sum(lista) / len(lista)

print(calcular_media_2(lista))


# 2
# Crea un programa que le pida dos números enteros al usuario y
# diga por consola si alguno de ellos es múltiplo del otro.
# La función debe llamarse es_multiplo().

def es_multiplo():
    numero_1 = int(input("Ingresar primer entero: "))
    numero_2 = int(input("Ingresar segundo entero: "))

    if numero_1 == 0 or numero_2 == 0:
        print("0 es múltiplo de todos los números =)")
    elif numero_1 % numero_2 == 0:
        print(f"{numero_1} es múltiplo de {numero_2}")
    elif numero_2 % numero_1 == 0:
        print(f"{numero_2} es múltiplo de {numero_1}")
    else:
        print("No son múltiplos")


es_multiplo()

# Es bisiesto
def calcular_si_es_bisiesto(year):
    if year % 400 == 0:
        print(f"El año {year} es bisiesto")
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f"El año {year} es bisiesto")

calcular_si_es_bisiesto(400)
calcular_si_es_bisiesto(1996)
calcular_si_es_bisiesto(2012)
calcular_si_es_bisiesto(2010)

# Separar
# Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas.
# La primera con los números pares, y la segunda con los números impares.
def separar(lista):
    par=[]
    impar=[]
    for num in lista:
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    par.sort()
    impar.sort()
    return par, impar


mi_lista = [1, 10, 5, 4, 3, 92, 1995, 2, 3, 4, 5, 6, 7, 8]
lista_de_pares, lista_de_impares = separar(mi_lista)
print(lista_de_pares)
print(lista_de_impares)