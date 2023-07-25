





class Televisor:

    def __init__(self, tamano=5, letra="F", precio_base=100):
        self.tamano = tamano
        self.letra = letra
        self.precio_base = precio_base


    def calcular_precio(self):
        precio = self.precio_base
        if self.tamano < 20:
            precio += 10

        if self.letra == "A":
            precio += 100

        return precio



tv = Televisor(tamano=10, letra="A")

print(tv.calcular_precio())