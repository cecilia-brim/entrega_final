from unicodedata import name
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate





urlpatterns = [

    path("" , views.Home ,name='Home'),
    path('busqueda' , views.busqueda_peliculas, name='busqueda'),
    path('resultado' , views.resultado_peliculas, name='resultado'), 
    path("quienesomos" , views.quienesomos, name='quienesomos'),
    path('login', views.login_request , name='Login'),
    path('register' , views.register , name = 'Register'),
    path('logout' , LogoutView.as_view(template_name = 'logout.html'), name='Logout'),
    path('editarPerfil' , views.editarPerfil , name="editarPerfil"),
    path('agregarAvatar' , views.agregarAvatar , name = "AgregarAvatar"),
    path('editarPerfil' ,views.editarPerfil, name="EditarPerfil"),
    path('agregarAvatar' , views.agregarAvatar , name = "AgregarAvatar"),
    path('post', views.post, name='post'),
    path('post_detail/<int:id>', views.post_detail, name='post_detail'),
    path('crear_post', views.crear_post, name='crear_post'),
    path('editar_post/<int:id>', views.editar_post, name='editar_post'),
    path('borrar_post/<int:id>', views.borrar_post, name='borrar_post'),
    path('buscar_post', views.buscar_post, name='buscar_post'),
    path('Perfil' , views.Perfil , name='Perfil'),
    path('Perfil/<str:username>/', views.Perfil , name='Perfil'),
    path('video', views.video , name= 'videoPresentacion'),
        
 ]

urlpatterns += staticfiles_urlpatterns()