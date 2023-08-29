from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Curso
from .forms import CursoFormulario

def cursos(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)

        print(mi_formulario)
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

        return render(request, "miApp/inicio.html")

    else:
        mi_formulario = CursoFormulario()


    return render(request, "miApp/cursos.html", {"mi_formulario": mi_formulario})


def inicio(request):
    return render(request, "miApp/inicio.html")

def buscar_camada(request):
    return render(request, "miApp/busqueda_camada.html")

def buscar(request):
    respuesta = f"Estoy buscando la camada: {request.GET['camada']}"
    if request.GET["camada"]:
        cursos = Curso.objects.filter(camada=request.GET["camada"])
        return render(request, "miApp/resultado_busqueda.html", {"cursos": cursos, "camada": request.GET["camada"]})
    else:
         return HttpResponse("No enviaste los datos")


def cursos_formulario(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)

        print(mi_formulario)
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

        return render(request, "miApp/inicio.html")

    else:
        mi_formulario = CursoFormulario()


    return render(request, "miApp/cursos_formulario.html", {"mi_formulario": mi_formulario})


def cursos_formulario_2(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
        curso.save()
    return render(request, "miApp/cursos_formulario.html")