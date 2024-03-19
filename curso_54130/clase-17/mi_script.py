import sys

print("hello!")
print()
print(sys.argv)
print(sys.argv, type(sys.argv))
print()

if sys.argv[1] == '1':
    print("El ususario ingresó 1")
else:
    print("No reconozco el número")

print()
