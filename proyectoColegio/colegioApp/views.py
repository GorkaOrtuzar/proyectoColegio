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
    #contexto = {'coles' = coles}
    #return render('listaColes.html', contexto, request )

