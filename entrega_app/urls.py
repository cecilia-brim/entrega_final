from django.urls import path
from . import views


urlpatterns = [
    path("" , views.index),
    path('busqueda' , views.busqueda_peliculas, name='busqueda'),
    path('resultado' , views.resultado_peliculas, name='resultado'), 
    
    
    ]