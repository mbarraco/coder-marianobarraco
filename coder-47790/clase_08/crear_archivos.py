mi_archivo = open("mi_primer_archivo.txt", "w")
mi_archivo.write("Esta es la primer linea que escribo!")
mi_archivo.write("Esta es la segunda linea que escribo!")
mi_archivo.writelines(
    [
        "Esta es la primer linea que escribo!\n",
        "Esta es la segunda linea que escribo!\n",
        "=)",
    ]
)
