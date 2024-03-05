import time


segundos_totales = range(60 * 5)

for segundo in segundos_totales:
    time.sleep(1)
    print(f"Quedan {60 * 5 - segundo} segundos")
