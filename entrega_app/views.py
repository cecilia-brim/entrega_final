from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from entrega_app.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from entrega_app.forms import UserEditForm , RegisterUserForm
from entrega_app.models import Avatar

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

def login_request(request):


    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario , password=contra)

            if user is not None: #no me funcionan los msjes VER
                login(request,user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render(request, 'Home.html' , {"url":avatares[0].imagen.url})
               

            else:
                return render(request, "login.html" , {"mensaje":"Error, datos incorrectos"})
        
        else:
            return render(request, "Home.html" , {"mensaje":"Error, formulario erroneo"})

    
    form = AuthenticationForm()

    return render(request, "login.html" , {"form": form})


def register(request):

    if request.method == 'POST':

        form= RegisterUserForm(request.POST)
        
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            #return HttpResponse("Usuario Creado")
            return render(request,"Home.html" , {"mensaje" : "Usuario Creado"})


    else:


       form = RegisterUserForm()

    return render(request, "register.html" , {"form" : form})


@login_required
def editarperfil(request):

    usuario = request.user

    if request.method == 'POST':
        pass
        miFormulario = UserEditForm(request.POST)
        return render(request , "Home.html")

    else:
        miFormulario = UserEditForm(initial ={'email' :usuario.email})

    return render(request, "editarPerfil.html" , {"miFormulario":miFormulario , "usuario":usuario})