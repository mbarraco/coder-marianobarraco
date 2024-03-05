mi_lista = [1, ("bilbo", "gandalf", "frodo"), "saruman", 99]

print("el mago blanco es: ", mi_lista[2])
print("el mago blanco en mayúscula: ", mi_lista[2].capitalize())

print("El portador del anillo es: ", mi_lista[1][2].upper())

mi_otra_lista = ["Harry", "Ron", "Hermione"]
print()
print(type(mi_otra_lista))
mi_tupla = tuple(mi_otra_lista)
print(type(mi_tupla), mi_tupla)
