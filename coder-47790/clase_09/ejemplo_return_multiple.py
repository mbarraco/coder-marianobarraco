def func():
    return 1, 2, "beta"


def func_exotica():
    return (1, 2), "beta", (2, 3)


mi_variable = func()

x, y, z = func()
# xx, yy = func()

print(mi_variable)

print(x)
print(y)
print(z)


xx = func_exotica()

print(xx)
