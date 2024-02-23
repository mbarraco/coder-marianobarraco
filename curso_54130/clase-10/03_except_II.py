def dividir_dos_numeros(a, b):
    return a / b


a = 40
b = 1
mi_lista = [1,2,3]

try: # si las siguientes lineas tiran un error:
    resultado = dividir_dos_numeros(a, b)
    print(resultado)
    print(mi_lista[9000000000000000000000])
except ZeroDivisionError:# entonces avisarle al usuario: "Tuviste un error, no se puede dividir por cero"
    print( "Tuviste un error, no se puede dividir por cero")
except IndexError:
    print( "Tuviste un error, no se puede acceder al elemento en la lista")



print()
print(" ---> Programa ejecutado con éxito <---")
print()