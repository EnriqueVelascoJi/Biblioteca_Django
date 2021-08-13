from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured

#Importamos los modelos
from .models import Venta, DetalleVenta

# Register your models here.
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    '''Admin View for Venta'''

    list_display = (
        'ven_id',
        'ven_forma_pago',
        'ven_fecha',
        'ven_impuesto',
        'ven_total',
    )
    list_filter = ('ven_forma_pago',)
    search_fields = (
        'ven_fecha',
        'ven_total',
    )
    ordering = ('ven_id',)

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    '''Admin View for DetalleVenta'''

    list_display = (
        'dv_id',
        'venta',
        'libro',
        'dv_cantidad',
        'dv_descuento'
    )
    # list_filter = ('',)
    search_fields = (
        'libro.lib_titulo',
    )
    ordering = ('dv_id',)
