# profe por que cuando ya el contacto estaba definido desde el principio su numero aparecia normal,
#pero el contacto que agregabamos despues su numero aparecia entre 'comillas?,
# Ingresar nombre del contacto: tobi
# ingresar numero telefonico: 123
# Agenda actualizada:  {'frodo': 222, 'drogo': 333, 'tobi': '123'}

agenda =  {'frodo': 222, 'drogo': 333}

print()
print(agenda)

nombre = input("Ingresar nombre del contacto: ")
numero = input("Ingresar numero telefonico: ")
numero = int(numero)
agenda[nombre] = numero

print()
print(agenda)
print(len(agenda))