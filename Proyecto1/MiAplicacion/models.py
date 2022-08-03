from django.db import models

# Create your models here.
class Pariente(models.Model):
    nombre = models.CharField(max_length=40)
    relacion = models.IntegerField()
    fecha = models.DateField()

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Tercera(models.Model):
    datochar = models.CharField(max_length=40)
    datoint = models.IntegerField()
    datofecha = models.DateField()