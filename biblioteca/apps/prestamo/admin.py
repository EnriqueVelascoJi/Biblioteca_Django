from django.contrib import admin

#Importamos los modelos
from .models import Prestamo, FichaPrestamo

# Register your models here.
@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    '''Admin View for Prestamo'''

    list_display = ('',)
    list_filter = ('',)
    search_fields = ('',)
    ordering = ('',)

@admin.register(FichaPrestamo)
class FichaPrestamoAdmin(admin.ModelAdmin):
    '''Admin View for FichaPrestamo'''

    list_display = ('',)
    list_filter = ('',)
    readonly_fields = ('',)
    ordering = ('',)