def decidir_si_es_bisiesto(year):
    if year % 4 == 0:
        if year % 100 == 0 and not year % 400 == 0:
            print(f"El año {year} no es bisiesto")
        else:
            print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")


# Suite de tests
decidir_si_es_bisiesto(2012)
print("El año 2012 es bisiesto")
print("\n")
decidir_si_es_bisiesto(2010)
print("El año 2010 no es bisiesto")
print("\n")
decidir_si_es_bisiesto(2000)
print("El año 2000 es bisiesto")
print("\n")
decidir_si_es_bisiesto(1900)
print("El año 1900 no es bisiesto")
print("\n")
decidir_si_es_bisiesto(400)
print("El año 400 es bisiesto")
