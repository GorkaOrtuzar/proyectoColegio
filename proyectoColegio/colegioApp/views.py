from http.client import HTTPResponse
from django.shortcuts import render
from .models import Colegio

# Create your views here.
def index(request):
    return HTTPResponse('primera vista')

def listaColegios(request):
    colegios = Colegio.objects.order_by('nombre')
    nombre_colegios = ','.join([colegio.nombre for coelgio in colegios])
    return HTTPResponse(nombre_colegios)

def detalleColegios(request, id_colegio):
    try:
        colegio = Colegio.objects.get(pk=id_colegio)
        trabajadores = colegio.trabajadores.all()

        cadenaDeTexto = f"{colegio.nombre} - CIF: {colegio.cif}\n"

        if trabajadores.exists():
            cadenaDeTexto += "Trabajadores:\n"
            for trabajador in trabajadores:
                cadenaDeTexto += f"{trabajador.nombre}, Antigüedad: {trabajador.antiguedad} años"
        else:
            cadenaDeTexto += "No hay trabajadores asociados a esta empresa"
        return HTTPResponse(cadenaDeTexto)
    except Colegio.DoesNotExist:
        return HTTPResponse("Empresa no encontrada")