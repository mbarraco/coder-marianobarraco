class Triangulo:

    def __init__(self, base, altura, lado_extra):
        self.base = base
        self.altura = altura
        self.lado_extra = lado_extra
        self.area = self.obtener_superficie()

    def obtener_superficie(self):
        superficie = (self.base * self.altura) / 2
        return superficie

    def __str__(self):
        return f"Triangulo: {self.base}, {self.altura}, {self.lado_extra}. Superficie: {self.obtener_superficie()}"


xx = Triangulo(3, 4, 5)
yy = Triangulo(10, 20, 40)

print(xx.obtener_superficie())
print(xx.area)


# si o si hay que llamar al función? no se puede llamar solo al parametro superficie?
