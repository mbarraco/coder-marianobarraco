c0 = set()
c1 = {1, 2, 3, 4, 4, "alpha"}

print("c0 ->", c0)
print("c1 ->", c1)

interseccion = c1.intersection(c0)
print("interseccion ->", interseccion)
print("-" * 90)

c0.add(1)
c0.add(3)
c0.add(90)
print("c0 ->", c0)
print("c1 ->", c1)
interseccion = c1.intersection(c0)
print("interseccion ->", interseccion)
print("-" * 90)

print("c0 ->", c0)
print("c1 ->", c1)
union = c1.union(c0)
print("union ->", union)
print("-" * 90)
print("c0 ->", c0)
print("c1 ->", c1)
print("es c0 subconjunto de c1: ", c0.issubset(c1))
c1.add(90)
print("c0 ->", c0)
print("c1 ->", c1)
print("es c0 subconjunto de c1: ", c0.issubset(c1))
print("es c1 subconjunto de c0: ", c1.issubset(c0))
print("-" * 90)

print("c0 incluye todos los elementos de de c1: ", c0.issuperset(c1))
print("c1 incluye todos los elementos de de c0: ", c1.issuperset(c0))
print("-" * 90)

print("c0 ->", c0)
print("c1 ->", c1)

print("La diferencia simétrica es: ", c0.symmetric_difference(c1))
