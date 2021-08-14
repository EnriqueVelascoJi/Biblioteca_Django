from django.urls import path

#Importamos las vistas
from . import views

app_name = 'libro_app'

urlpatterns = [
    path('', views.Inicio.as_view(), name='inicio'),    
    path('add/', views.LibroCreateView.as_view(), name='crear_libro'),    
]