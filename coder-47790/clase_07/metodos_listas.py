xx = list(range(5, 10))
print(xx)
xx.clear()
print(xx)

print("-" * 90)

xx = list(range(5, 10))
yy = [1, 2, 3]
print(xx)
print(yy)
yy.append(xx)
print(yy)
print(len(yy))

yy.extend(xx)
print(yy)
print(len(yy))
# desafio: hacer una funcion que sea una version propia del "extend"
print("-" * 90)

xx = list(range(5, 10))
print(xx)
xx.insert(2, "Messi")
print(xx)
xx.reverse()
print(xx)
print("-" * 90)
xx = [3, 5, 7, 1, 0, -90]
xx.sort()
print(xx)
xx.sort(reverse=True)
print(xx)