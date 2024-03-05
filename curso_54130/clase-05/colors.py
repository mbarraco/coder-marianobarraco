print("hola")


colors = {
    "green": "\033[92m",
    "red": "\033[91m",
    "yellow": "\033[93m",  # ANSI code for yellow
    "end": "\033[0m",
}

print("\033[92m" + "HOLA" + "\033[0m")
print("\033[91m" + "HOLA" + "\033[0m")
print("\033[93m" + "HOLA" + "\033[0m")
