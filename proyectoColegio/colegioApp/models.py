from django.db import models

# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()
    provincia = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    imagenCiudad = models.URLField(max_length=600, null= True, blank=True)  

    def __str__(self):
        return self.nombre

class Colegio(models.Model):
    nombre = models.CharField(max_length=100)
    ubi = models.CharField(max_length=100)
    cursoMin = models.CharField(max_length=50)
    cursoMax = models.CharField(max_length=50)
    modeloEstudio = models.CharField(max_length=1)
    Ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE , related_name="colegio", null=True)
    imagenColegio = models.URLField(max_length=600, null= True, blank=True)   
    def __str__(self):
        return self.nombre
   
class Profesor(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    fechaNac = models.DateTimeField()
    antiguedad = models.PositiveIntegerField()
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE , related_name="profesores")
    imagenProfesor = models.URLField(max_length=600, null= True, blank=True) 
       
    def __str__(self):
        return self.nombre

   