# 1 - Iprimir las primeras 5 películas

f = open("disney_movies.csv", "r")

contador = 0
for fila in f.readlines():
    fila = fila.split(",")
    if contador == 0:
        contador += 1
        continue
    print(f"Pelicula numero: {contador}")
    print(f"""
        nombre: {fila[0]}
        fecha: {fila[1]}
        genero: {fila[2]}
        recaudacion: {int(fila[5]) / 100}
        """
    )
    contador += 1
    if contador == 6:
        break

f.close()