from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured

#Importamos el modelo
from .models import Libro

# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    '''Admin View for Libro'''

    list_display = (
        'lib_id',
        'lib_titulo',
        'lib_autor',
        'lib_isbn',
        'lib_editorial',
        'lib_copias_venta',
        'lib_copias_servicio',
        'lib_precio'
    )
    list_filter = ('lib_editorial',)
    search_fields = (
        'lib_titulo',
        'lib_autor',
        'lib_isbn',
        'lib_editorial',
    )
    ordering = ('lib_id',)
