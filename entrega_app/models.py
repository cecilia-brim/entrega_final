from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Peliculas(models.Model):
    
    actor_nombre = models.CharField(max_length=40)
    actor_apellido = models.CharField(max_length=40)
    pelicula_nombre = models.CharField(max_length=40)
    pelicula_año = models.IntegerField()
    pelicula_link = models.URLField(max_length=2500)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares' , null= True , blank = True)


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    intro = models.TextField()
    mensaje = models.TextField() #modificar
    imagen = models.ImageField(null=True, upload_to='post', default='placeholder.png')
    #autor = models.CharField(max_length=60) #agregar
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):

    autor = models.ForeignKey(Post, on_delete = models.CASCADE, null=False, blank=False)
    email = models.EmailField()
    contenido = models.TextField(max_length=1500)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.autor) + ' | ' + str( self.fecha)


