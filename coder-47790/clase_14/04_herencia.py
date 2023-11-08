
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


class PatoConApellido(Animal):
    """Me 'robo' todo lo que implemente `Animal`"""

    especie = "Pato blanco patagonico"

    def __init__(self, nombre, apellido):
        super().__init__(nombre)
        self.apellido = apellido

    def nadar(self):
        print("Estoy nadando!")

    def saludar(self):
        print(f"Mi nombre es {self.xx} {self.apellido} y soy un {self.especie}")


class Ave(Animal): # Juan

    especie = "Condor"

    def volar(self):
        print("Estoy volando!")


class Tigre(Animal):

    especie = "Sumatra"

    def cazar(self):
        print("Estoy Cazando patos")



mi_ave = Ave("Condorito")
mi_ave.saludar()
mi_ave.volar()

print("_" * 90)
print("_" * 90)

mi_tigre = Tigre("Tony")
mi_tigre.saludar()
mi_tigre.cazar()

print("_" * 90)
print("_" * 90)

mi_pato = Pato("Dalmacio")
mi_pato.saludar()

print("_" * 90)
print("_" * 90)
mi_pato = PatoConApellido("Dalmacio", "Velez")
mi_pato.saludar()
