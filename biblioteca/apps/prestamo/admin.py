from django.contrib import admin

#Importamos los modelos
from .models import Prestamo, FichaPrestamo

# Register your models here.
@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    '''Admin View for Prestamo'''

    list_display = (
        'pre_id',
        'pre_hora_prestamo',
        'pre_hora_regreso',
        'pre_fecha'
    )
    list_filter = ('pre_fecha',)
    search_fields = (
        'pre_hora_prestamo',
        'pre_hora_regreso',
        'pre_fecha'
    )
    ordering = ('pre_id',)

@admin.register(FichaPrestamo)
class FichaPrestamoAdmin(admin.ModelAdmin):
    '''Admin View for FichaPrestamo'''

    list_display = (
        'fp_id',
        'prestamo',
        'libro',
        'fp_estado',
    )
    search_fields = ('libro.lib_titulo',)
    list_filter = ('fp_estado',)
    ordering = ('fp_id',)