
# Pedir al usuario que ingrese 2 numeros, sumarlos y motrarlos por pantalla
# Si el usuario ingresa algo que no puede ser interpretado como numero
# entonces mostrarle un mensaje de error y pedirle que ingrese números nuevamente

while True:
    try:
        a = int(input("num a = "))
        b = int(input("num b = "))
    except ValueError:
        print("ese valor no es un numero")
    else:
        print(a+b)
        break
    finally:
        print("Esta línea se ejecutará siempre!")

# Ejercicio: rediseñar este código para que si el valor de "a" fue
#            guardado correctamente, entonces no vuelva a pedirlo.