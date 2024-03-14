# 1 - Encontrar la película que mayor cantidad de dinero ajustado por inflacion generó
# 2 - Encontrar la película que menor cantidad de dinero ajustado por inflacion generó

f = open("disney_movies.csv")

print("1 -> ", f.readline())


# 1. Recorrer cada una de las <filas> : OK
# 2. revisar <la última columna> de cada una de  las 580: OK
# 3. hasta encontrar la mas grande

for movie in f.readlines():
    movie_data = movie.split(",")
    recaudacion = int(movie_data[5])
    print(recaudacion)



f.close()