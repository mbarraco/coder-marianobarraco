paises_campeones_del_mundo = {
    1990: "Alemania",
    1994: "Brasil",
    1998: "Francia",
    2002: "Brasil",
    2006: "Italia",
    2010: "España",
    2014: "Alemania",
    2018: "Francia",
}

print(
    f"Los paises que salieron campeones de la Copa Mundial de la FIFA desde el año 1990 al 2018 son: {paises_campeones_del_mundo}"
)

print()

año_de_la_copa = input(
    "Introduzca el año del cual quisieras saber el campeon de la copa mundial: "
)

año_de_la_copa = int(año_de_la_copa)

campeon_del_año = paises_campeones_del_mundo.get(año_de_la_copa, "No encontrado")

print()

print(f"En el año {año_de_la_copa} fue campeon de la copa mundial: {campeon_del_año}")
