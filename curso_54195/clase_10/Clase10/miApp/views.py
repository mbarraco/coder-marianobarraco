from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from random import randint


def cursos(request):
    return render(request, "miApp/cursos.html")


def cursos_enriquecido(request):
    return render(
        request,
        "miApp/cursos_enriquecido.html",
        {"nombre": "elefante", "numero_aleatorio": randint(0, 100)}
    )

def cursos_formulario(request):

    print("*" * 90)
    print(request.method)
    print("*" * 90)

    if request.method == "POST":
        # podemos crear un curso
        print(request.POST)
        return render(request, "miApp/cursos.html")
    else:
        return render(request, "miApp/curso_formulario.html")