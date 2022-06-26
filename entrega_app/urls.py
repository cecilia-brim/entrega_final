from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("" , views.Home ,name='Home'),
    path('busqueda' , views.busqueda_peliculas, name='busqueda'),
    path('resultado' , views.resultado_peliculas, name='resultado'), 
    path("quienesomos" , views.quienesomos, name='quienesomos'),
    path('login' , views.login_request , name='Login'),
    path('register' , views.register , name = 'Register'),
    path('logout' , LogoutView.as_view(template_name = 'logout.html'), name='Logout'),
    path('editarPerfil' , views.editarperfil , name="EditarPerfil"),
    path('agregarAvatar' , views.agregarAvatar , name = "AgregarAvatar"),

    ]

urlpatterns += staticfiles_urlpatterns()