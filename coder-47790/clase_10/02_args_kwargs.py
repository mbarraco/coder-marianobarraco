def mi_func_1(*args):
    for element in args:
        print(element)


def mi_func_2(*args, **kwargs):
    for element in args:
        print(element)

    for key, value in kwargs.items():
        print(f"{key}: {value}")


mi_func_2("alpha", "beta", "gamma", arg_1="omega", arg_2="omicron")
