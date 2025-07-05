from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import QuerySet
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Ruta
from .forms import RutaForm, CustomUserCreationForm, EmailAuthenticationForm
from django.contrib.auth.models import User

# Create your views here.

@login_required
def index(request):
    rutas: QuerySet = Ruta.objects.all()  # type: ignore
    context = {'rutas': rutas}
    return render(request, 'index.html', context)

@login_required
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

@login_required
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

def registro_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.username}! Registro exitoso.')
            return redirect('pins:index')
        else:
            messages.error(request, 'Por favor corrige los errores para registrarte.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(username=user_obj.username, password=password)
            except Exception:
                user = None
            if user is not None:
                login(request, user)
                messages.info(request, f'Has iniciado sesión como {user.first_name} {user.last_name}.')
                return redirect('pins:index')
            else:
                messages.error(request, 'Correo o contraseña incorrectos.')
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')
    else:
        form = EmailAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('pins:login')


