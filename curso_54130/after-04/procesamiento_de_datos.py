ruta_del_archivo = "disney_movies.csv"
f = open("disney_movies.csv")
print("1 -> ", f.readline())

recaudaciones = []
titulos = []
for movie in f.readlines():
    recaudacion = movie.split(",")[-1]
    titulo = movie.split(",")[0]
    recaudacion = int(recaudacion)
    recaudaciones.append(recaudacion)
    titulos.append(titulo)

recaudacion_maxima = max(recaudaciones)
print(recaudacion_maxima)
index = recaudaciones.index(recaudacion_maxima)
titulo_de_recaudacion_maxima = titulos[index]
print(titulo_de_recaudacion_maxima)
f.close()