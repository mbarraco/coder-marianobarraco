
class Animal:

    especie = "Ninguna especie"

    def __init__(self, nombre):
        self.xx = nombre

    def saludar(self):
        print(f"Hola, soy {self.xx} y pertenzco a {self.especie}")


class Pato(Animal):
    """Me 'robo' todo lo que implemente `Animal`"""

    especie = "Cauquén"

    def nadar(self):
        print("Estoy nadando!")

    def saludar(self):
        print("No tengo ganas de saludar!")

mi_pato = Pato("Dalmacio")
mi_pato.saludar()
mi_pato.nadar()