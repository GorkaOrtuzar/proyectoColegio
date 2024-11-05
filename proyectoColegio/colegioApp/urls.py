from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listaC'),


    path('listadeCiudades/', views.listaColes, name="listaCiudades"),






    ##DESDE AQUI LOS HA HECHO ASIER 
    path('listadeColegios/', views.listaColegioConPlantillas, name="listaColes"),
    path('detalleColes/<int:id_colegio>', views.detalleColegioPlantillasAsier, name="detalleColes"),
    ##HASTA AQUI LOS HA HECHO ASIER 



    path('listadoDeProfesores/', views.listaProfes, name='listaProf'),


    path('listaCiudades/<int:id_empresa>', views.detalleCiudad, name='detalle'),
    ###path('Colegio/<int:id_empresa>', views.detalleColegioConPlantillas  , name='detalle'),
    #path('detalleTrabajador/<int:id_trabajador>', views.detalleProfesor, name='detalleTrabajador'),

]
