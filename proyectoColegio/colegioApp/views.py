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

def listaColes(request):
    coles = Colegio.objects.order_by('nombre')
    cadenaDeTexto = ', '.join([e.nombre for e in coles])
    return HTTPResponse(cadenaDeTexto)

def listaCiudad(request):
    ciudades = Ciudad.objects.order_by('nombre')
    cadenaDeTexto = ', '.join([e.nombre for e in ciudades])
    return HTTPResponse(cadenaDeTexto)

def listaProfes(request):
    profes = Profesor.objects.order_by('nombre')
    cadenaDeTexto = ', '.join([e.nombre for e in profes])
    return HTTPResponse(cadenaDeTexto)


def index(request):
    return render(request, 'index.html')


def detalleCiudad(request, id_ciudad):
    ciudad = get_object_or_404(Ciudad, pk=id_ciudad)
    contexto = {'ciudad': ciudad}
    return render(request, 'detalleCiudad.html', contexto)


def detalleCiudadConPlantillas(request, id_ciudad):
    ciudad = get_object_or_404(Ciudad, pk=id_ciudad)
    contexto = {'ciudad': ciudad}
    return render(request, 'detalleCiudad.html', contexto)


def detalleColegioConPlantillas(request, id_colegio):
    colegio = get_object_or_404(Colegio, pk=id_colegio)
    contexto = {'colegio': colegio}
    return render(request, 'detalle.html', contexto)

def detalleProfesorConPlantillas(request, id_profesor):
    profesor = get_object_or_404(Profesor, pk=id_profesor)
    contexto = {'profesor': profesor}
    return render(request, 'detalle.html', contexto)






##esta de aqui abajo funciona LAS HA HECHO ASIER 

def listaColegioConPlantillas(request):
    colegios = Colegio.objects.order_by('nombre')
    contexto = {'colegio_list': colegios}
    return render(request, 'listaColegio.html', contexto)



def detalleColegioPlantillasAsier(request, id_colegio):
    colegio = get_object_or_404(Colegio, pk=id_colegio)
    contexto = {'colegio': colegio}
    return render(request, 'detalleColegio.html', contexto)


##hasta aqui abajo funciona LAS HA HECHO ASIER 





def detalle(request, nombre_colegio):
    return HttpResponse(f"Consultando el colegio {nombre_colegio}.")


def nosehacerviews(request, id_colegio):
    return HttpResponse(f"Información del colegio con ID = {id_colegio}.")




