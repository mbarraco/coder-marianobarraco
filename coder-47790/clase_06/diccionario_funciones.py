dict_1 = {1: "one", 2: "two", 3: "three", 4: "four"}
print(dict_1)
del dict_1[2]
print(dict_1)
dict_1.clear()
print(dict_1)

dict_2 =  {1: "one", 2: "two", 3: "three", 4: "four"}

print("-" * 90)
xx = dict_2.get(3)
print(xx)
yy = dict_2.get(90, "No pude encontrar el valor")
print(yy)

print("Fin del programa")