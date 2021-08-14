from django.shortcuts import render

#Importamos las vitas
from django.views.generic import CreateView, TemplateView

#Importamos el modelo
from .models import Libro

# Create your views here.

#Vista de Inicio

class Inicio(TemplateView):
    template_name = "inicio.html"

#Creación
class LibroCreateView(CreateView):
    model = Libro
    template_name = "libro/crear_libro.html"

    context_object_name = 'libro'

    fields = ('__all__')

