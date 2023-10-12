from pprint import pprint
from time import sleep

contactos = {
    "Harry Potter": {
        "nombre": "Harry",
        "apellido": "Potter",
        "email": "harry@hogwarts.edu",
        "edad": 17,
        "pais": "Reino Unido"
    },
    "Hermione Granger": {
        "nombre": "Hermione",
        "apellido": "Granger",
        "email": "hermione@hogwarts.edu",
        "edad": 17,
        "pais": "Reino Unido"
    },
    "Ron Weasley": {
        "nombre": "Ron",
        "apellido": "Weasley",
        "email": "ron@hogwarts.edu",
        "edad": 17,
        "pais": "Reino Unido"
    },
    "Albus Dumbledore": {
        "nombre": "Albus",
        "apellido": "Dumbledore",
        "email": "dumbledore@hogwarts.edu",
        "edad": 115,
        "pais": "Reino Unido"
    },
    "Minerva McGonagall": {
        "nombre": "Minerva",
        "apellido": "McGonagall",
        "email": "minerva@hogwarts.edu",
        "edad": 70,
        "pais": "Reino Unido"
    },
    "Draco Malfoy": {
        "nombre": "Draco",
        "apellido": "Malfoy",
        "email": "draco@hogwarts.edu",
        "edad": 17,
        "pais": "Reino Unido"
    },
    "Sirius Black": {
        "nombre": "Sirius",
        "apellido": "Black",
        "email": "sirius@hogwarts.edu",
        "edad": 35,
        "pais": "Reino Unido"
    },
    "Luna Lovegood": {
        "nombre": "Luna",
        "apellido": "Lovegood",
        "email": "luna@hogwarts.edu",
        "edad": 16,
        "pais": "Reino Unido"
    },
    "Nymphadora Tonks": {
        "nombre": "Nymphadora",
        "apellido": "Tonks",
        "email": "tonks@hogwarts.edu",
        "edad": 25,
        "pais": "Reino Unido"
    },
    "Cedric Diggory": {
        "nombre": "Cedric",
        "apellido": "Diggory",
        "email": "cedric@hogwarts.edu",
        "edad": 17,
        "pais": "Francia"
    },
    "Dolores Umbridge": {
        "nombre": "Dolores",
        "apellido": "Umbridge",
        "email": "umbridge@hogwarts.edu",
        "edad": 50,
        "pais": "Reino Unido"
    },
    "Bellatrix Lestrange": {
        "nombre": "Bellatrix",
        "apellido": "Lestrange",
        "email": "bellatrix@hogwarts.edu",
        "edad": 45,
        "pais": "Francia"
    },
    "Tom Riddle": {
        "nombre": "Tom",
        "apellido": "Riddle",
        "email": "voldemort@hogwarts.edu",
        "edad": 65,
        "pais": "Reino Unido"
    },
    "Rubeus Hagrid": {
        "nombre": "Rubeus",
        "apellido": "Hagrid",
        "email": "hagrid@hogwarts.edu",
        "edad": 60,
        "pais": "Reino Unido"
    },
    "Severus Snape": {
        "nombre": "Severus",
        "apellido": "Snape",
        "email": "snape@hogwarts.edu",
        "edad": 38,
        "pais": "Reino Unido"
    }
}


for nombre_de_contacto, datos_de_contacto in contactos.items():

    edad = datos_de_contacto["edad"]
    if edad >= 18:
        print(nombre_de_contacto, edad)
    else:
        print(f"{nombre_de_contacto} es menor a 18 años")
    print("-" * 90)
    sleep(1)



