from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),


    ##path('listadeCiudades/', views.listaColes, name="listaCiudades"),

    ##DESDE AQUI LOS HA HECHO ASIER 
    path('listadeColegios/', views.listaColegioView.as_view(), name="listaColegio"),
    path('detalleColes/<int:pk>', views.detalleColegioView.as_view(), name="detalleColes"),
    ##HASTA AQUI LOS HA HECHO ASIER 

    path('listadeProfes/', views.listaProfesorView.as_view(), name='listaProfesor'),
    path('detalleProfes/<int:pk>', views.detalleProfesorView.as_view(), name='detalleProfes'),

    ##path('listadeCiudades/', views.listaCiudadConPlantillas, name='listaCiudad'),
    ##path('detalleCiudad/<int:id_ciudad>', views.detalleCiudadConPlantillas, name='detalleCiudad'),

    ##DE LAS VISTAS BASADAS EN CLASES
    path('listadeCiudades/', views.listaCiudadView.as_view(), name='listaCiudad'),
    path('detalleCiudades/<int:pk>', views.detalleCiudadView.as_view(), name='detalleCiudad'),

    #INVENTADAS POR ASIER
    #path('listaCoches/', views.listaCoche.as_view(), name='listaCoche'),
    #path('detalleCoches/', views.detailCoche.as_view(), name='detalleCoche'),

]
