
class Cuadrado:

    # inicializate a ti mismo considerando que tu lado es lo que diga el usuario que te crea y tu color también.
    #                 "SELF"
    def __init__(self, lado, color):
        self.lado = lado
        self.superficie = lado * lado
        self.perimetro = lado * 4
        self.color = color

    def saludar(self):
        print(f"Hola soy un cuadrado de {self.lado} cm de lado y color {self.color}")


mi_cuadrado = Cuadrado(lado=6, color="blanco")
mi_otro_cuadrado = Cuadrado(8, "negro")
mi_cuadradote = Cuadrado(8000, "dorado")

# print(f"la superficie de tu figura es: {mi_cuadrado.superficie}")
# print(f"el perimetro de tu figura es: {mi_cuadrado.perimetro}")

mi_cuadrado.saludar()
mi_otro_cuadrado.saludar()
mi_cuadradote.saludar()