from django.db import models

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()