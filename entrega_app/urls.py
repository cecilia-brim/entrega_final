from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path("" , views.Home ,name='Home'),
    path('busqueda' , views.busqueda_peliculas, name='busqueda'),
    path('resultado' , views.resultado_peliculas, name='resultado'), 
    path("quienesomos" , views.quienesomos, name='quienesomos')
    
    ]

urlpatterns += staticfiles_urlpatterns()