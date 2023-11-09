import sys


print("Este es un script")
print("_" * 90)
print(sys.argv)
print("_" * 90)
print(sys.argv[0])
print("_" * 90)
if len(sys.argv) > 1:
    print(sys.argv[1])
print("_" * 90)

for i, argumento in enumerate(sys.argv):
    print(i, argumento, type(argumento))
