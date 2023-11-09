class Triangulo:

    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c


    def __str__(self):
        return f"Triangulo: [{self.a}, {self.b}, {self.c}]"

class TrianguloConPerimetro(Triangulo):

    def calcular_perimetro(self):
        return self.a + self.b + self.c


class TrianguloEquilatero(TrianguloConPerimetro):

    def __init__(self, lado):
        super().__init__(lado, lado, lado)