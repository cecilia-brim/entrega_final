from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Peliculas(forms.Form):
    
    actor_nombre = forms.CharField(max_length=40)
    actor_apellido = forms.CharField(max_length=40)
    pelicula_nombre = forms.CharField(max_length=40)
    pelicula_año = forms.IntegerField()
    pelicula_link = forms.URLField(max_length=2500)


class RegisterUserForm(UserCreationForm):

    email= forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña' , widget = forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña' , widget = forms.PasswordInput)

    last_name = forms.CharField()
    first_name= forms.CharField()

    class Meta:
        model= User
        fields= ['username' , 'email' , 'password1' , 'password2' , 'last_name' , 'first_name']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):

    email= forms.EmailField(label="Modificar")
    password1 = forms.CharField(label= 'Contraseña' , widget = forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña' , widget = forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta: #sirve para asociar a tablas de user
        model = User
        fields= ['email' , 'password1' , 'password2' , 'last_name' , 'first_name']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField()
#height_field=None, width_field=None, max_length=100