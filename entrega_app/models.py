from django.db import models
from django.contrib.auth.models import User

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
