from geometria.triangulos import Triangulo, TrianguloEquilatero


equilatero = Triangulo(4, 4, 4)
otro_equilatero = TrianguloEquilatero(900)

print(equilatero)
print(otro_equilatero)
print(otro_equilatero.calcular_perimetro())