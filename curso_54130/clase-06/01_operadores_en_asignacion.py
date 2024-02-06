import time


longitud = 0
mi_texto = "Alta en el cielo"

for letra in mi_texto:
    time.sleep(.3)
    # longitud = longitud + 1
    longitud += 1
    print(letra, longitud)

print(f"La longitud de '{mi_texto}' es {longitud}")

