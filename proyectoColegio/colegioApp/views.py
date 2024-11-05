from http.client import HTTPResponse
from django.shortcuts import render
from .models import Colegio

# Create your views here.


## TENEIS QUE HACER 6 VISTAS (1 MAS OPCIONAL)

## 1 VISTA DE DETALLE DE COLEGIO Y UNA VISTA DE LISTA DE TODOS LOS COLEGIOS 
## 1 VISTA DE DETALLE DE PROFESOR Y UNA VISTA DE LISTA DE TODOS LOS PROFESORES 
## 1 VISTA DE DETALLE DE CIUDAD Y UNA VISTA DE LISTA DE TODOS LOS CIUDAD 


## OPCIONAL 

### INDEX VISTA --> PARA PODER ELEGIR CUALQUIERA DE LAS 3 VISTA DE LISTA 



def index(request):
    return HTTPResponse('primera vista')

def listaColes(request):
    coles = Colegio.objects.order_by('nombre')
    cadenaDeTexto = ', '.join([e.nombre for e in coles])
    return HTTPResponse(cadenaDeTexto)

def listaProfes(request):
    profesores = Profesor.objects.all()
    cadenaDeTexto = "Lista de Trabajadores:\n"

    if profesores.exists():
        for profesor in profesores:
            cadenaDeTexto += (
                f"- ID: {profesor.id}, "
                f"Nombre: {profesor.nombre}, "
                f"Fecha de Nacimiento: {profesor.fecha_nacimiento}, "
                f"Antigüedad: {profesor.antiguedad} años, "
                f"Asignaturas: {profesor.asignaturas}\n"
            )
    else:
        cadenaDeTexto += "No hay profesores registrados."
    return HttpResponse(cadenaDeTexto) 

def detalleColegio(request, id_colegio):
    colegio = get_object_or_404(Colegio, pk=id_colegio)
    profesores = colegio.profesores.all()
    cadenaDeTexto = f"{colegio.nombre}\n"
    cadenaDeTexto += "Trabajadores:\n"

    if profesores.exists():
        for profesor in profesores:
            cadenaDeTexto += f"- {profesor.nombre}, Antigüedad: {profesor.antiguedad} años\n"
    else:
        cadenaDeTexto += "No hay profesores asociados a esta colegio."
    return HttpResponse(cadenaDeTexto)

def index(request):
    return render(request, 'index.html')

def listaTrabajadores2(request):
    trabajadores = Trabajador.objects.order_by('nombre')
    contexto = {'lista_trabajadores': trabajadores}
    return render(request, 'listaT.html', contexto)



