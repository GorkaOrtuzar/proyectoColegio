from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from .models import Colegio,Profesor,Ciudad
##Modificación segunda entrega --> si no hacemos el import da un warnign de que no esta definido
from django.views.generic import ListView, DetailView

# Create your views here.


## TENEIS QUE HACER 6 VISTAS (1 MAS OPCIONAL)

## 1 VISTA DE DETALLE DE COLEGIO Y UNA VISTA DE LISTA DE TODOS LOS COLEGIOS 
## 1 VISTA DE DETALLE DE PROFESOR Y UNA VISTA DE LISTA DE TODOS LOS PROFESORES 
## 1 VISTA DE DETALLE DE CIUDAD Y UNA VISTA DE LISTA DE TODOS LOS CIUDAD 

## OPCIONAL 

### INDEX VISTA --> PARA PODER ELEGIR CUALQUIERA DE LAS 3 VISTA DE LISTA 



def index(request):
    return render(request, 'index.html')

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


##LISTAS BASADAS EN CLASES
class DetalleCiudadView(DetailView): ##object
    model = Ciudad
    template_name= 'detalleCiudad.html'
    context_object_name = 'ciudad' ##nombre del contexto

class ListaProfesoresView (ListView): #object_list
    model = Profesor
    template_name= 'listaProfesor.html'
    context_object_name = 'lista_trabajadores'
    queryset = Profesor.objects.order_by('nombre')

##INVENTADAS POR ASIER
class detailCoche(DetailView):
    modelo = Coche
    template_name = 'detalle_coche.html'
    context_object_name = 'coche'

class listaCoche(ListView):
    modelo = Coche
    template_name = 'list_coche.html'


