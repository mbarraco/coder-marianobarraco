import sys

# Obtener los argumentos de línea de comandos
argumentos_del_script = sys.argv

print(f"Los argumentos ingresados son: {sys.argv}")

for i, arg in enumerate(argumentos_del_script):
    print(f"Argumento {i}: {arg}")