# Kenneth dijo:
# definimos una variable tirangulo que una base de 3, una altura de  4 y otro lado de 5
class Triangulo:

    # def inicializar_el_triangulo_en_cuestion(self):
    def __init__(triangulo_en_construccion):
        print("------- creacion -------")
        triangulo_en_construccion.base = 3
        triangulo_en_construccion.altura = 4
        triangulo_en_construccion.lado_extra = 5

    def obtener_superficie(el_triangulo_en_cuestion):
        print("------ superficie ------")
        return 309209472390790823749821398429837498123948712389489712347891239874


# triangulo = Construir un triangulo de lados 3, 4 y 5 cuya base es 4 y su altura 3

print("1")
xx = Triangulo()
print("2")
superficie = xx.obtener_superficie()
print("3")
print(superficie)
print("4")
print(f"la base del triángulo es {xx.base}")


# Ejercicio de Pedro Svriz
# Entonces, en POO no se pueden creár directamente un triangulo,
# que en la terminal nos salga un triangulo, o un cuadrado solamente
# diciendo sus pixeles de ancho y alto?
