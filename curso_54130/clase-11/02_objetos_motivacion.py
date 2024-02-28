"""

Cálculo de Área:
    Triángulo: (base x altura) /2
    Rectángulo: base x altura
    Trapecio: (base mayor + base menor) * altura / 2

Cálculo de Perímetro:
    Triángulo: a + b + c
    Rectángulo: 2 * base + 2 * altura
    Trapecio: a + b + c + d

"""

# # A
# lado1, lado2, lado3 = 3, 4, 5

# B
triangulo = {
    "lado1" : 3,
    "lado2" : 4,
    "lado3" : 5

}
def calcular_area_geometrica(base, altura):
    area = (base * altura) / 2
    print(area)
    return area

calcular_area_geometrica(triangulo["lado1"], triangulo["lado2"])
calcular_area_geometrica(triangulo["lado1"], triangulo["lado3"])