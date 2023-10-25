

def mi_func(parametro_1):
    print(f"El parametro 1 es: {parametro_1}")

def mi_func_2(parametro_1, parametro_2):
    print(f"El parametro 1 es: {parametro_1}")
    print(f"El parametro 2 es: {parametro_2}")



mi_func("alpha")
print("_" * 90)
mi_func_2("alpha", "beta")
print("_" * 90)
mi_func_2("beta", "alpha")
print("_" * 90)
mi_func_2(parametro_2="beta", parametro_1="alpha")
print("_" * 90)
mi_func_2(parametro_1="alpha", parametro_2="beta")
print("_" * 90)
mi_func_2("beta", parametro_2="alpha")

