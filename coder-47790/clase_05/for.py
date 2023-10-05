xx = ["a", "b", "c", "d", "e"]

# para cada elemento en xx hace lo siguiente:
#     imprimi el elemento
for el in xx:
    print(el)


for el in xx:
    if el == "c":
        print(f"--->  {el.upper()}")
    else:
        print(el)