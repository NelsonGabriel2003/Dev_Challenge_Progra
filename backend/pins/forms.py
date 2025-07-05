from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
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

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'})
    )
    last_name = forms.CharField(
        required=True,
        label='Apellido',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu apellido'})
    )
    email = forms.EmailField(
        required=True,
        label='Correo institucional',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@puce.edu.ec'})
    )

    password1 = forms.CharField(
        label='Contraseña',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        help_text='''<ul>
            <li>Tu contraseña no puede ser demasiado similar a tu información personal.</li>
            <li>Debe contener al menos 8 caracteres.</li>
            <li>No puede ser una contraseña comúnmente utilizada.</li>
            <li>No puede ser completamente numérica.</li>
        </ul>'''
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repite la contraseña'}),
        strip=False,
        help_text='Introduce la misma contraseña para verificación.'
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
        # No incluimos username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@puce.edu.ec'):
            raise ValidationError('Solo se permiten correos institucionales de la PUCE (@puce.edu.ec).')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este correo electrónico ya está registrado.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        # Ahora el username será igual al email completo
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Correo institucional',
        widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'correo@puce.edu.ec'})
    )

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError('Esta cuenta está inactiva.', code='inactive')
