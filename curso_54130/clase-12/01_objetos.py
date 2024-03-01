# Ejercicio: crear una clase Rectángulo  con los mismos métodos que Triángulo
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = self.obtener_superficie()

    def obtener_superficie(self):
        superficie = self.base * self.altura
        return superficie

    def __str__(self):
        return f"Rectangulo: {self.base}, {self.altura}, {self.base}, {self.altura}. Superficie: {self.obtener_superficie()}"


xx = Rectangulo(3, 4)
yy = Rectangulo(10, 20)

print(xx.obtener_superficie())
print(yy.area)
