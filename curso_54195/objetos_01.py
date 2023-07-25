


class FiguraDeMadera:

    material = "madera"



class FiguraGeometrica:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __str__(self):
        return f"Soy una figura geométrica"


class NuestroTriangulo(FiguraGeometrica, FiguraDeMadera):

    def calcular_superficie(self):
        return self.base * self.altura / 2

    def __str__(self):
        return f"Hola soy un triangulo de {self.material}, de base {self.base} y altura {self.altura}"


class NuestroRectangulo(FiguraGeometrica, FiguraDeMadera):

    def calcular_superficie(self):
        return self.base * self.altura


t_1 = NuestroTriangulo(2, 4) # superficie es 4
t_2 = NuestroTriangulo(2, 10)
r_1 = NuestroRectangulo(2, 4)



# Somos una empresa instaladora de pisos y cobramos $6 el metro cuadrado
def cotizar(figura):
    return 6 * figura.calcular_superficie()


print(t_1)