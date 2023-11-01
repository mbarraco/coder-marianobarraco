
class Cuadrado:

    # inicializate a ti mismo considerando que tu lado es lo que diga el usuario que te crea.
    # "SELF"
    def __init__(self, lado, color):
        self.lado = lado
        self.superficie = lado * lado
        self.perimetro = lado * 4
        self.color = color

    def saludar(self):
        print(f"Hola soy un cuadrado de {self.lado} cm de lado")

mi_cuadrado = Cuadrado(lado=6, color="blanco")

print(f"la superficie de tu figura es: {mi_cuadrado.superficie}")
print(f"el perimetro de tu figura es: {mi_cuadrado.perimetro}")

print(type(mi_cuadrado))

mi_cuadrado.saludar()