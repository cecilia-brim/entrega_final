from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from entrega_app.models import *

# Create your views here.

def Home(request):
 return render(request, 'Home.html')


def quienesomos(request):
      return render (request ,"quienesomos.html") 

def facebook (request):
   return render(request , "www.facebook.com")      



def busqueda_peliculas(request):

    return render(request, 'busqueda_peliculas.html')

def resultado_peliculas(request):

    if request.GET['actor_nombre']:

        actor_nombre = request.GET['actor_nombre']
        peliculas = Peliculas.objects.filter(actor_nombre__icontains = actor_nombre)
        return render(request, 'resultado_peliculas.html', {'peliculas': peliculas})

    else:
        respuesta = 'Datos ingrseados inválidos'
    
    return HttpResponse(respuesta)
