from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured

#Importamos los modelos
from .models import Venta, DetalleVenta

# Register your models here.
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    '''Admin View for Venta'''

    list_display = ('',)
    list_filter = ('',)
    search_fields = ('',)
    ordering = ('',)

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    '''Admin View for DetalleVenta'''

    list_display = ('',)
    list_filter = ('',)
    search_fields = ('',)
    ordering = ('',)
