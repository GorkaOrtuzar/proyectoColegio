from django.contrib import admin
from .models import Colegio, Profesor,Ciudad

##admin.site.register(Ciudad)
##admin.site.register(Colegio)
##admin.site.register(Profesor)

class CiudadAdmin(admin.ModelAdmin):
    fieldsets = [ 
        (None, {'fields':['nombre']}),
        ('Sitio geografico', {'fields': ['pais', 'provincia', 'codigoPostal']}), 
        ('Imagen', {'fields': ['imagenCiudad']}),]
    list_display = ('nombre', 'provincia')
admin.site.register(Ciudad, CiudadAdmin)

class ColegioAdmin(admin.ModelAdmin):
    fieldsets= [
        (None, {'fields':['nombre']}),
        ('Sitio geografico', {'fields': ['Ciudad', 'ubi']}),
        ('Curso y Modelo', {'fields': ['cursoMin', 'cursoMax', 'modeloEstudio']}),
        ('Imagen', {'fields': ['imagenColegio']}),]
    list_display = ('nombre', 'Ciudad', 'modeloEstudio')
admin.site.register(Colegio, ColegioAdmin)
    

class ProfesorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos personales', {'fields': ['dni', 'nombre', 'fechaNac']}),
        ('Datos adicionales', {'fields': ['colegio', 'antiguedad']}),
        ('Imagen', {'fields': ['imagenProfesor']}),]
    list_display = ('nombre', 'colegio')
admin.site.register(Profesor, ProfesorAdmin)

    