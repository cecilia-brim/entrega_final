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
    #path('blogPost', views.BlogPostView.as_view(), name='blogPost'),
    #path('<slug>:<slug>/', views.PostDetailView.as_view(), name='post-detail'),
 ]

urlpatterns += staticfiles_urlpatterns()