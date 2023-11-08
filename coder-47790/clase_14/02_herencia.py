
class Animal:

    def __init__(self, nombre):
        self.xx = nombre

    def saludar(self):
        print(f"Hola, soy {self.xx}")


class Pato(Animal):
    """Me 'robo' todo lo que implemente `Animal`"""

    def nadar(self):
        print("Estoy nadando!")


mi_pato = Pato("Dalmacio")
mi_pato.saludar()
mi_pato.nadar()