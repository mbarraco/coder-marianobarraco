# Ejemplo: calcular el promedio entre 6, 9 y 10 e imprimirlo por pantalla
mi_primer_valor = 6
mi_segundo_valor = 9
mi_tercer_valor = 10
mi_promedio = (mi_primer_valor + mi_segundo_valor + mi_tercer_valor) / 3
print("El promedio es:", mi_promedio)
print("El promedio es:")
print(mi_promedio)

# ejemplo 2 Funcion

def calcular_promedio():
    mi_primer_valor = 8
    mi_segundo_valor = 10
    promedio = (mi_primer_valor + mi_segundo_valor) / 2
    print("promedio es: ", promedio)

calcular_promedio()

# Repaso clase 1
mi_variable_numero = 1
mi_variable_texto = "uno mas uno"
mi_otra_variable_de_texto = ": es dos"
mi_texto_final = mi_variable_texto + mi_otra_variable_de_texto
print("." * 90)
print(mi_texto_final)
print("." * 90)
print(mi_texto_final[-8:])
print("." * 90)
print(type(mi_texto_final))
print("." * 90)

# Presentacion de tuplas y listas
mi_lista = [89, "ochenta y nueve", 12, -4, "t"]
mi_tupla = (89, "ochenta y nueve", 12, -4, "t")

print("_" * 90)
print(mi_lista)
print("_" * 90)
print(type(mi_lista))
print("_" * 90)
print(mi_tupla)
print("_" * 90)
print(type(mi_tupla))
print("_" * 90)

# Promedio con tuplas o listas
mis_notas = (10, 10, 8, 8)
mis_notas = [10, 10, 8, 8]
cantidad_de_notas = len(mis_notas)
suma_de_mis_notas = sum(mis_notas)
promedio = suma_de_mis_notas / cantidad_de_notas
print("cantidad de notas: ",cantidad_de_notas)
print("suma de mis notas: ", suma_de_mis_notas)
print("promedio", promedio)

print(mis_notas)
print(mis_notas[0])
print(mis_notas[0:2])
print(mis_notas[-3:])