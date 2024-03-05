class Triangulo:

    def __init__(self, base, altura, lado_extra):
        self.base = base
        self.altura = altura
        self.lado_extra = lado_extra

    def obtener_superficie(self):
        superficie = (self.base * self.altura) / 2
        return superficie

    def __str__(self):
        return f"Triangulo: {self.base}, {self.altura}, {self.lado_extra}"


xx = Triangulo(3, 4, 5)
yy = Triangulo(4, 7, 20)
ww = Triangulo(41, 79, 250)
zz = Triangulo(45, 67, 520)

print(xx)
print(yy)
print(ww)
print(zz)
