from django.contrib import admin
from .models import Ruta

# Register your models here.

@admin.register(Ruta)

class RutaAdmin(admin.ModelAdmin):
    pass
