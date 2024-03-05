def dividir_dos_numeros(a, b):
    return a / b


a = 40
b = 40

try:  # si las siguientes lineas tiran un error:
    resultado = dividir_dos_numeros(a, b)
    print(resultado)
except:  # entonces avisarle al usuario: "Tuviste un error, no se puede dividir por cero"
    print("Tuviste un error, no se puede dividir por cero")


print()
print(" ---> Programa ejecutado con éxito <---")
print()
