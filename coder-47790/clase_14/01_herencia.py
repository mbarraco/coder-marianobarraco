
class Animal:

    def __init__(self, nombre):
        self.xx = nombre

    def saludar(self):
        print(f"Hola, soy {self.xx}")


class PatoDeMadera:

    def __init__(self, zz):
        pass


class Pato(Animal):
    """Me 'robo' todo lo que implemente `Animal`"""
    pass


mi_pato = Animal("Dalmacio")
mi_pato.saludar()

mi_pato_2 = Pato("Albertina")
mi_pato_2.saludar()
