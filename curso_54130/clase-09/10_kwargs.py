def saludar(**kwargs):
    for posicion, nombre in kwargs.items():
        print(f"hola {nombre},  {posicion}!")


saludar(jugador_1="Bilbo", jugador_2="Frodo", jugador_3="Pippin")
print()
saludar(
    embajador="Anselmo",
    jugador_1="Bilbo",
    jugador_2="Frodo",
    jugador_3="Pippin",
    madre="roberta",
)
