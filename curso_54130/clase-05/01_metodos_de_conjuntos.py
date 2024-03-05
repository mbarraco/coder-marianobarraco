ALPHA = {1, 2, 3, 4}
BETA = {2, 3}
GAMA = {100, 101}
print()

# INTERSECTION_UPDATE
interseccion = ALPHA.intersection_update(BETA)
print("La interseccion de ALPHA y BETA es:", interseccion)
print("ALPHA quedo: ", ALPHA)
print()


# INTERSECTION
ALPHA = {1, 2, 3, 4}
interseccion = ALPHA.intersection(BETA)
print("La interseccion de ALPHA y BETA es:", interseccion)
print("ALPHA quedo: ", ALPHA)
print()

# DIFFERENCE_UPDATE
# EPSILON = ALPHA.difference(BETA)
ALPHA.difference_update(BETA)
print("ALPHA quedo: ", ALPHA)
print()

# DIFFERENCE
ALPHA = {1, 2, 3, 4}
# EPSILON = ALPHA.difference(BETA)
EPSILON = ALPHA - BETA
print("ALPHA - BETA", EPSILON)
print("ALPHA quedo: ", ALPHA)
print()

# UNION
OMEGA = ALPHA.union(GAMA)
print("Union de ALPHA y GAMA", OMEGA)
print()

# ISSUPERSET
print("ALPHA contiene a BETA:", ALPHA.issuperset(BETA))
print("GAMA contiene a BETA:", GAMA.issuperset(BETA))
print()


# ISSUBSET
print("BETA es subconjunto con ALPHA:", BETA.issubset(ALPHA))
print("BETA es subconjunto con GAMA:", BETA.issubset(GAMA))
print()

# ISDISJOINT
print("ALPHA es disjunto con BETA:", ALPHA.isdisjoint(BETA))
print("ALPHA es disjunto con GAMA:", ALPHA.isdisjoint(GAMA))
print()


# COPY
mi_conjunto = BETA.copy()
print(mi_conjunto)
mi_conjunto.add("7")
print(mi_conjunto)
print(BETA)
