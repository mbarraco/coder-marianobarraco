
from time import sleep

def xx(mi_numero):
    resto_de_divir_con_dos = mi_numero % 2
    if resto_de_divir_con_dos == 0:
        print(f"{mi_numero} es un numero par")
    else:
        print(f"{mi_numero} es un numero impar")


for i in range(10000000):
    # sleep(1.5)
    xx(i)
