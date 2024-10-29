from django.db import models

# Create your models here.
class Colegio(models.Model):
    nombre = models.CharField(max_length=100)
    cif = models.CharField(max_length=9)

    def _str_(self):
        return self.nombre

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    antiguedad = models.PositiveIntegerField()
    empresa = models.ForeignKey(Empresa, related_name='trabajadores', on_delete=models.CASCADE)

    def _str_(self):
        return self.nombre
