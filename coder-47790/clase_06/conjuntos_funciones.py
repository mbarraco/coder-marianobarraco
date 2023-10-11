
xx = set()
print("1 -> ", xx)

xx.add(1)
print("2 -> ", xx)

xx.update(["alpha", "beta", "gamma", "phi", "epsilon", "omega"])
print("3 -> ", xx)

xx.discard("betania")
xx.remove("beta")
print("4 -> ", xx)

xx.pop()
print("5 -> ", xx)

print("6 -> ", "alpha" in xx)
print("7 -> ", "beta" in xx)


print("8 -> ", len(xx))
xx.clear()
print("9 -> ", len(xx))
print("10-> ", xx)