class Triangulo:

    def __init__(self, base, altura, lado_extra):
        print("------- creacion -------")
        self.base = base
        self.altura = altura
        self.lado_extra = lado_extra

    def obtener_superficie(self):
        print("------ superficie ------")
        # Falta una implementación correcta!!!
        superficie = (self.base * self.altura) / 2
        return superficie


# triangulo = Construir un triangulo de lados 3, 4 y 5 cuya base es 4 y su altura 3

xx = Triangulo(3, 4, 5)
yy = Triangulo(4, 7, 20)
print(xx == yy)
print(
    f"la base del triangulo xx es {xx.base} y su superficie es: {xx.obtener_superficie()}"
)
print(
    f"la base del triangulo yy es {yy.base} y su superficie es: {yy.obtener_superficie()}"
)

# Ejercicio de Pedro Svriz
# Entonces, en POO no se pueden creár directamente un triangulo,
# que en la terminal nos salga un triangulo, o un cuadrado solamente
# diciendo sus pixeles de ancho y alto?
