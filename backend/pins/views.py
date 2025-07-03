from django.shortcuts import render
from .models import Ruta

# Create your views here.

def index(request):
    rutas = Ruta.objects.all()
    context = {'rutas': rutas}
    return render(request, 'index.html')


