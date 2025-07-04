from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import QuerySet
from .models import Ruta
from .forms import RutaForm

# Create your views here.

def index(request):
    rutas: QuerySet = Ruta.objects.all()  # type: ignore
    context = {'rutas': rutas}
    return render(request, 'index.html', context)

def agregar_ruta(request):
    if request.method == 'POST':
        form = RutaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Ruta agregada exitosamente!')
            return redirect('pins:index')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = RutaForm()
    
    context = {'form': form}
    return render(request, 'agregar_ruta.html', context)


