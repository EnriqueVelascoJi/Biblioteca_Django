from django.contrib import admin

#Importamos los modelos externos
from .models import Renta, FichaRenta

# Register your models here.
#Admin de Renta
@admin.register(Renta)
class RentaAdmin(admin.ModelAdmin):
    '''Admin View for Renta'''

    list_display = (
        'ren_id',
        'socio',
        'ren_fecha_renta',
        'ren_fecha_regreso',
    )
    # list_filter = ('',)
    search_fields = (
        'socio.soc_nombre',
        'ren_fecha_renta',
        'ren_fecha_regreso',
    )
    ordering = ('ren_id',)

#Admin de Ficha de Renta
@admin.register(FichaRenta)
class FichaRentaAdmin(admin.ModelAdmin):
    '''Admin View for FichaRenta'''

    list_display = (
        'fr_id',
        'renta',
        'libro',
        'fr_estado',
    )
    list_filter = ('fr_estado',)
    search_fields = (
        'libro.lib_titulo',
        'fr_estado',)
    ordering = ('fr_id',)
