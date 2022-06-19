from django import forms


class Peliculas(forms.Form):
    
    actor_nombre = forms.CharField(max_length=40)
    actor_apellido = forms.CharField(max_length=40)
    pelicula_nombre = forms.CharField(max_length=40)
    pelicula_año = forms.IntegerField()
    pelicula_link = forms.URLField(max_length=2500)