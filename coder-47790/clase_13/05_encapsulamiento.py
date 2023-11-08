

class Animal:

    especie = "No definida"

    def __init__(self, nombre):
        self.xx = nombre
        self.__zz = nombre

    def __saludar(self):
        print(f"hola soy {self.__zz} y estoy contento!")

    def _presentarse(self):
        self.__saludar()
        print("Ya llegué")



animal = Animal("pedro")

print(animal.especie)
print(animal.zz)
# print(animal.__zz)
# print(animal.__saludar())
animal._presentarse()

