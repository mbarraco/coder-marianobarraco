print()
agenda_1 = {}
agenda_1["frodo"] = 222
agenda_1["drogo"] = 333
agenda_1["legolas"] = 999

agenda_2 = {"gandalf": 322, "elrond": 112, "legolas": 555}

print("agenda 1", agenda_1)
print("agenda 2", agenda_2)
print()

agenda_1.update(agenda_2)
print("agenda 1", agenda_1)
print("agenda 2", agenda_2)
print()
