
from django import forms
from .models import Ruta

class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = [
            'titulo',
            'descripcion',
            'punto_inicio',
            'punto_destino',
            'tipo_transporte',
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Ruta Segura desde la PUCE al CCI en Trole'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe los pasos, paradas, y cualquier consejo útil.'}),
            'punto_inicio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Universidad PUCE (Av. 12 de Octubre)'}),
            'punto_destino': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Centro Comercial Iñaquito (CCI)'}),
            'tipo_transporte': forms.Select(attrs={'class': 'form-control'}),
        }
