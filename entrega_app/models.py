from django.db import models

# Create your models here.
class Peliculas(models.Model):
    
    actor_nombre = models.CharField(max_length=40)
    actor_apellido = models.CharField(max_length=40)
    pelicula_nombre = models.CharField(max_length=40)
    pelicula_año = models.IntegerField()
    pelicula_link = models.URLField(max_length=2500)