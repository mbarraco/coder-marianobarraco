
from time import sleep



def decidir_si_es_par_o_impar(mi_numero):
    resto_de_divir_con_dos = mi_numero % 2
    if resto_de_divir_con_dos == 0:
        print(f"{mi_numero} es un numero par")
    else:
        print(f"{mi_numero} es un numero impar")


for i in range(10):
    sleep(1.5)
    decidir_si_es_par_o_impar(i)
