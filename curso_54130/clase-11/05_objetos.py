# Kenneth dijo:
# definimos una variable tirangulo que una base de 3, una altura de  4 y otro lado de 5
class Triangulo:

    # def inicializar_el_triangulo_en_cuestion(self):
    def __init__(triangulo_en_construccion):
        print("------- creacion -------")
        triangulo_en_construccion.base = 3
        triangulo_en_construccion.altura = 4
        triangulo_en_construccion.lado_extra = 5

    def obtener_superficie(triangulo_ya_construido):
        print("------ superficie ------")
        # Falta una implementación correcta!!!
        superficie = (triangulo_ya_construido.base * triangulo_ya_construido.altura) / 2
        return superficie


# triangulo = Construir un triangulo de lados 3, 4 y 5 cuya base es 4 y su altura 3

print("1")
xx = Triangulo()
print("2")
print(f"la base del triángulo es {xx.base} y su altura es {xx.altura}")
print(
    f"la base del triángulo es {xx.base} y su altura es {xx.altura} y tiene un lado extra que mide {xx.lado_extra}"
)
print(
    f"la base del triángulo es {xx.base} y su altura es {xx.altura} y su superficie es {xx.obtener_superficie()}"
)


# Ejercicio de Pedro Svriz
# Entonces, en POO no se pueden creár directamente un triangulo,
# que en la terminal nos salga un triangulo, o un cuadrado solamente
# diciendo sus pixeles de ancho y alto?
