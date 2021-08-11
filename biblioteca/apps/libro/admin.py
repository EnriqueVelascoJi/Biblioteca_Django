from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured

#Importamos el modelo
from .models import Libro

# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    '''Admin View for Libro'''

    list_display = ('',)
    list_filter = ('',)
    search_fields = ('',)
    ordering = ('',)
