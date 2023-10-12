dict_1 = {"harry": "potter", "frodo": "baggins"}

print(dict_1["frodo"])
# print(dict_1["bilbo"]) # da error "KeyError"
print(dict_1.get("bilbo"))
print(dict_1.get("bilbo", "Bolsón"))