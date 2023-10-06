from time import sleep


for numero in range(10):
    sleep(1)
    print(numero)
    if numero == 2:
        print(".... 1")
        continue
    elif numero == 8:
        print(".... 2")
        # break
        pass
else:
    print("..... 3")
    print("Se terminó de iterar y numero vale: ", numero)
