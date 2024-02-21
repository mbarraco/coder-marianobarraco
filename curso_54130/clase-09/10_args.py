def sumar(*args):
    print(args)
    suma = 0
    for arg in args:
        suma += arg
    print("suma: ", suma)

print()
sumar(1)

print()
sumar(1, 2, 3, 4, 5, 6, 7 , 8)