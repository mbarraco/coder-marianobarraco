from django.contrib import admin
from django.urls import path

from .views import cursos, cursos_formulario, buscar_camada, buscar

urlpatterns = [
    path("inicio/", cursos, name="inicio"),
    path("cursos/", cursos, name="cursos"),
    path("cursosFormulario/", cursos_formulario, name="cursos-formulario"),
    path("buscarCamada/", buscar_camada, name="buscar-camada"),
    path("buscar/", buscar, name="buscar"),
]
