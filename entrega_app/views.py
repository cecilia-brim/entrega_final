from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'entrega_app/index.html')