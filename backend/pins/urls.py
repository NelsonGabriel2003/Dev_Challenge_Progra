from django.urls import path
from . import views

app_name = 'pins'

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar-ruta/', views.agregar_ruta, name='agregar_ruta'),
    path('editar-ruta/<int:ruta_id>/', views.editar_ruta, name='editar_ruta'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]