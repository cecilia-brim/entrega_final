from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comentario


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

class Crear_Post_Form(forms.ModelForm):
    titulo = forms.CharField(max_length=255)
    intro = forms.CharField(max_length=255)
    mensaje = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()

    class Meta:
        model = Post
        fields = ('titulo', 'intro', 'mensaje','imagen')

class Post_Validate(forms.Form):
    titulo = forms.CharField(max_length=255)
    intro = forms.CharField(max_length=255)
    mensaje = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()
    date_added = forms.DateField()

class Post_Edit_Validate(forms.Form):
    titulo = forms.CharField(max_length=255)
    intro = forms.CharField(max_length=255)
    mensaje = forms.CharField(widget=forms.Textarea)
    

class Editar_Post_Form(forms.ModelForm):
    titulo = forms.CharField(max_length=255)
    intro = forms.CharField(max_length=255)
    mensaje = forms.CharField(widget=forms.Textarea)
    

    class Meta:
        model = Post
        fields = ('titulo', 'intro', 'mensaje')