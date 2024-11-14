from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),


    ##path('listadeCiudades/', views.listaColes, name="listaCiudades"),

    ##DESDE AQUI LOS HA HECHO ASIER 
    path('listadeColegios/', views.listaColegioConPlantillas, name="listaColegio"),
    path('detalleColes/<int:id_colegio>', views.detalleColegioPlantillasAsier, name="detalleColes"),
    ##HASTA AQUI LOS HA HECHO ASIER 

    path('listadeProfes/', views.listaProfesConPlantillas, name='listaProfesor'),
    path('detalleProfes/<int:id_profesor>', views.detalleProfesorConPlantillas, name='detalleProfes'),


    path('listadeCiudades/', views.listaCiudadConPlantillas, name='listaCiudad'),
    path('detalleCiudad/<int:id_ciudad>', views.detalleCiudadConPlantillas, name='detalleCiudad'),

    ##DE LAS VISTAS BASADAS EN CLASES
    path('detalleCiudadView/<int:pk>', views.DetalleCiudadView.as_view(), name='detalleCiudadView'),

    #INVENTADAS POR ASIER
    #path('listaCoches/', views.listaCoche.as_view(), name='listaCoche'),
    #path('detalleCoches/', views.detailCoche.as_view(), name='detalleCoche'),

]
