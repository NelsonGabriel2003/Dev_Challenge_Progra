from django.shortcuts import render, redirect, get_object_or_404
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

def editar_ruta(request, ruta_id):
    ruta = get_object_or_404(Ruta, id=ruta_id)
    if request.method == 'POST':
        form = RutaForm(request.POST, instance=ruta)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Ruta actualizada exitosamente!')
            return redirect('pins:index')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = RutaForm(instance=ruta)
    
    context = {
        'form': form,
        'ruta': ruta  
    }
    return render(request, 'agregar_ruta.html', context)


