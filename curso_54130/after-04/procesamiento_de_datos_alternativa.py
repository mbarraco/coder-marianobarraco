ruta_del_archivo = "disney_movies.csv"
f = open("disney_movies.csv")
print("1 -> ", f.readline())


recaudacion_maxima = 0
pelicula = "no encontrada!"
for movie in f.readlines():
    recaudacion = movie.split(",")[-1]
    recaudacion = int(recaudacion)
    if recaudacion > recaudacion_maxima:
        recaudacion_maxima = recaudacion
        pelicula = movie


print(pelicula)