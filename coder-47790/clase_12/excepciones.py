

def dividir(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return "Hubo un error"

def dividir_mejorada(a, b):
    try:
        resultado =  a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero!"
    except TypeError:
        return "Tienes una incompatibilidad en tus argumentos!"
    else:
        print("................")
        return resultado
    finally:
        print("________________")

def dividir_mejorada_otra_vez(a, b):
    try:
        resultado =  a / b
    except ZeroDivisionError as e:
        return f"Hubo un error matematico: {e}"
    except TypeError as e:
        return f"Tienes una incompatibilidad en tus argumentos!: {e}"
    else:
        print("................")
        return resultado
    finally:
        print("________________")



# ZeroDivisionError
# TypeError
# print(dividir_mejorada(4, 2))
# print(dividir_mejorada(2, 4))
print(dividir_mejorada_otra_vez(2, 0))
print(dividir_mejorada_otra_vez(2, "a"))