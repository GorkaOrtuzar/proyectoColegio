from django.db import models

# Create your models here.

class Ciudad(models.Model):
    id = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    codigoPostal = models.IntegerField(max_length=5)
    provincia = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

class Colegio(models.Model):
    id = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    ubi = models.CharField(max_length=100)
    cursoMin = models.CharField(max_length=50)
    cursoMax = models.CharField(max_length=50)
    modeloEstudio = models.CharField(max_length=1)
    Ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE , related_name="colegio")   

   

   
class Profesor(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    fechaNac = models.DateTimeField()
    antiguedad = models.PositiveIntegerField()
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE , related_name="profesores")   


   