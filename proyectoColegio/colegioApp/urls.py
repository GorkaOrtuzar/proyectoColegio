from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listaC'),


    ##path('listadeCiudades/', views.listaColes, name="listaCiudades"),

    ##DESDE AQUI LOS HA HECHO ASIER 
    path('listadeColegios/', views.listaColegioConPlantillas, name="listaColes"),
    path('detalleColes/<int:id_colegio>', views.detalleColegioPlantillasAsier, name="detalleColes"),
    ##HASTA AQUI LOS HA HECHO ASIER 

    path('listadeProfesores/', views.listaProfesConPlantillas, name='listaProfes'),
    path('detalleProfes/<int:id_profesor>', views.detalleProfesorConPlantillas, name='detalleProfes'),


    path('listadeCiudades/', views.listaCiudadConPlantillas, name='listaCiudad'),
    path('detalleCiudad/<int:id_ciudad>', views.detalleCiudadConPlantillas, name='detalleCiudad'),


    #path('listaCiudades/<int:id_empresa>', views.detalleCiudad, name='detalle'),
    #path('Colegio/<int:id_empresa>', views.detalleColegioConPlantillas  , name='detalle'),
    #path('detalleTrabajador/<int:id_trabajador>', views.detalleProfesor, name='detalleTrabajador'),

]
