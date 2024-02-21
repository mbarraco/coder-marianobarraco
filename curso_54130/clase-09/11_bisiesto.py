def es_bisiesto(year):
    # Los años bisiestos son multiplos de 4
    # Los multiplos de 100 NO SON BISIESTOS
    if year % 4 == 0: # (es True si year es multiplo de 4)
        print(f"{year} es bisiesto")


    else:
        print(f"{year} NO es bisiesto")



es_bisiesto(1999)
print()

es_bisiesto(100)
print()

es_bisiesto(2024)
print()

es_bisiesto(2023)
print()

es_bisiesto(10000)
print()

es_bisiesto(200)
print()

es_bisiesto(400)
print()

es_bisiesto(800)
print()