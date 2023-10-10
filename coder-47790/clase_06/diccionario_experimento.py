

dict_1 = {1: "one", 2: "two"}
dict_2 = dict_1
dict_3 = dict_1.copy()

print("dict_1 --> ", dict_1)
print("dict_2 --> ", dict_2)
print("dict_3 --> ", dict_3)
print("-" * 90)

dict_1[2] = "XX"
print("dict_1 --> ", dict_1)
print("dict_2 --> ", dict_2)
print("dict_3 --> ", dict_3)
# print("-" * 90)