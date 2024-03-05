agenda = {}
agenda["frodo"] = 222
agenda["drogo"] = 333

print()
print("Agenda inicial", agenda)
print()

nombre = input("Ingresar nombre del contacto: ")
numero = input("Ingresar numero telefonico: ")

agenda[nombre] = numero
print()
print("Agenda actualizada", agenda)

print()
contacto_para_buscar = input("Ingresar nombre del contacto para buscar: ")
telefono = agenda[contacto_para_buscar]

# print("el telefono de tu contacto es: ", telefono)
# print(f"el telefono de {contacto_para_buscar} es: ", telefono)
print(f"el telefono de {contacto_para_buscar} es: {telefono}")
# print("el telefono de {contacto_para_buscar} es: {telefono}")
