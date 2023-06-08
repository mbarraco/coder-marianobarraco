from collections import namedtuple
una_tupla = ("mariano", "barraco", "marianobarraco@gmail.com")
print(una_tupla[2])
Alumno = namedtuple("Alumno", ["nombre", "appelido", "email"])
alumno_mariano = Alumno("mariano", "barraco", "marianobarraco@gmail.com")
print(alumno_mariano[2])
print(alumno_mariano.email)


from collections import Counter
mis_calificaciones = [1,1,2,3,2,3,5,2,9,7,8,5,3,3,4,5,6,7,8,8,8,8]
contador = Counter(mis_calificaciones)
print(contador)
print(contador[8])
contador_palabra = Counter("abracadabra")
print(contador_palabra)


from datetime import datetime


ahora = datetime.now()
print(ahora)
print(ahora.minute)
print(ahora.year)


navidad_2021 = datetime(2021, 12, 25)
print(navidad_2021)

print(navidad_2021.strftime('%A %d %b %Y'))