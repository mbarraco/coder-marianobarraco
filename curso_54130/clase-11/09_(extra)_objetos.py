class Triangulo:

    def __init__(self, base, altura, lado_extra):
        self.base = base
        self.altura = altura
        self.lado_extra = lado_extra

    def obtener_superficie(self):
        superficie = (self.base * self.altura) / 2
        return superficie

    def __str__(self):
        for i in range(self.altura + 1):
            print("*" * self.base)
        return ""


xx = Triangulo(1, 2, 5)
yy = Triangulo(3, 4, 5)
ww = Triangulo(4, 6, 9)
zz = Triangulo(5, 7, 9)

print(xx)
print(yy)
print(ww)
print(zz)
