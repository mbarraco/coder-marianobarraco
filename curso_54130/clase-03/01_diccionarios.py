agenda = {}
agenda["frodo"] = 222
agenda["drogo"] = 333

print()
print("Agenda inicial", agenda)

contacto_para_buscar = input("Ingresar nombre del contacto para buscar: ")
contacto_para_buscar = contacto_para_buscar.lower()

#################################################### BUSCAR ELEMENTO EN DICCIONARIO
# telefono = agenda[contacto_para_buscar]  # FORMA 1
# telefono = agenda.get(contacto_para_buscar) # FORMA 2
telefono = agenda.get(contacto_para_buscar, "NO ENCONTRADO")  # FORMA 3


print(f"el telefono de {contacto_para_buscar} es: {telefono}")


print()
print()
print("Programa finalizado con éxito")
