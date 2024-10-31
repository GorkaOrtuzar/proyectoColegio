from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listaC'),



    path('listadeColegios', views.listaColes, name="listaColes"),
]
