def mi_func(aa, b=9):
    aa = aa + b
    print(aa)


a = 80
mi_func(a)
print(a)


print("_" * 40)


def mi_func_2(una_lista):
    una_lista.append("1")
    print(una_lista)


mi_lista = []
mi_func_2(mi_lista)
print(mi_lista)
