from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from .models import Colegio,Profesor,Ciudad

# Create your views here.


## TENEIS QUE HACER 6 VISTAS (1 MAS OPCIONAL)

## 1 VISTA DE DETALLE DE COLEGIO Y UNA VISTA DE LISTA DE TODOS LOS COLEGIOS 
## 1 VISTA DE DETALLE DE PROFESOR Y UNA VISTA DE LISTA DE TODOS LOS PROFESORES 
## 1 VISTA DE DETALLE DE CIUDAD Y UNA VISTA DE LISTA DE TODOS LOS CIUDAD 

## OPCIONAL 

### INDEX VISTA --> PARA PODER ELEGIR CUALQUIERA DE LAS 3 VISTA DE LISTA 



def index(request):
    return HTTPResponse('primera vista')

    profesor = get_object_or_404(Profesor, pk=id_profesor)
    contexto = {'profesor': profesor}
    return render(request, 'detalle.html', contexto)

##COLEGIOS
def listaColegioConPlantillas(request):
    colegios = Colegio.objects.order_by('nombre')
    contexto = {'colegio_list': colegios}
    return render(request, 'listaColegio.html', contexto)

def detalleColegioPlantillasAsier(request, id_colegio):
    colegio = get_object_or_404(Colegio, pk=id_colegio)
    contexto = {'colegio': colegio}
    return render(request, 'detalleColegio.html', contexto)

##PROFESORES
def listaProfesConPlantillas(request):
    profesores = Profesor.objects.order_by('nombre')
    contexto = {'profesor_list' : profesores}
    return render(request, 'listaProfesor.html', contexto)

def detalleProfesorConPlantillas(request, id_profesor):
    profesor = get_object_or_404(Profesor, pk=id_profesor)
    contexto = {'profesor': profesor}
    return render(request, 'detalleProfesor.html', contexto)

##CIUDADES
def listaCiudadConPlantillas(request):
    ciudad = Ciudad.objects.order_by('nombre')
    contexto = {'ciudad_list' : ciudad}
    return render(request, 'listaCiudad.html', contexto)

def detalleCiudadConPlantillas(request, id_ciudad):
    ciudad = get_object_or_404(Ciudad, pk=id_ciudad)
    contexto = {'ciudad': ciudad}
    return render(request, 'detalleCiudad.html', contexto)


def detalle(request, nombre_colegio):
    return HttpResponse(f"Consultando el colegio {nombre_colegio}.")

def nosehacerviews(request, id_colegio):
    return HttpResponse(f"Información del colegio con ID = {id_colegio}.")




