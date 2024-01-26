# ACTIVIDAD EN CLASE
# Desafío de Listas

# Descripción de la actividad:
# En esta actividad, podrás poner en práctica todo lo aprendido durante la sesión.

# Dadas dos listas LISTA1 y LISTA2 debes realizar las siguientes tareas:
lista_1 = []
lista_2 = []
# 1. Añade a la LISTA1 el int 456789 y luego el string "Hola Mundo"
lista_1.append(123456789)
lista_1.append("hola mundo")
# 2. Luego añade a la LISTA2 el string "Hola y Adios" y luego el int 5555
lista_2.append("Hola y Adios")
lista_2.append(5555)
# 3. Genera una LISTA3 con todos los elementos de la LISTA1 sin considerar el último elemento
# lista_3 = [lista_1[0]]
lista_3 = lista_1[:-1]
# 4. Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último elemento
lista_4 = lista_2[1:-1]
# 5. Finalmente, genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3
lista_5 = lista_4 + lista_3
### extra para el punto 5
lista_5_bis = []
lista_5_bis.extend(lista_4)
lista_5_bis.extend(lista_3)

print("lista_1:", lista_1)
print("lista_2:", lista_2)
print("lista_3:", lista_3)
print("lista_4:", lista_4)
print("lista_5:", lista_5)
print("lista_5_bis:", lista_5_bis)


# extra
lista_5_bis.extend(["9999999999", "8888888888"])
print("lista_5_bis:", lista_5_bis)
