

def calcular_fibonacci(posicion):
    if posicion == 1:
        return 1
    elif posicion == 2:
        return 1
    else:
        return calcular_fibonacci(posicion-1) + calcular_fibonacci(posicion-2)
    # elif posicion == 3:
    #     # return    calcular_fibonacci(2)     +      calcular_fibonacci(1)
    #     return calcular_fibonacci(posicion-1) + calcular_fibonacci(posicion-2)
    # elif posicion == 4:
    #     # return    calcular_fibonacci(2)     +      calcular_fibonacci(1)
    #     return calcular_fibonacci(posicion-1) + calcular_fibonacci(posicion-2)
    # elif posicion == 5:
    #     # return    calcular_fibonacci(2)     +      calcular_fibonacci(1)
    #     return calcular_fibonacci(posicion-1) + calcular_fibonacci(posicion-2)


xx = calcular_fibonacci(10)
print(xx)