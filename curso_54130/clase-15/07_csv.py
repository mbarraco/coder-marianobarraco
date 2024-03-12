# 1 - Encontrar la película que mayor cantidad de dinero ajustado por inflacion generó
# 2 - Encontrar la película que menor cantidad de dinero ajustado por inflacion generó

f = open("disney_movies.csv")

print("1 -> ", f.readline())


for movie in f.readlines():
    movie_data = movie.split(",")
    print(movie_data[5])
    break



f.close()