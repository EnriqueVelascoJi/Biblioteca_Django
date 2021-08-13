from django.contrib import admin

#Importar el modelo
from .models import Multa

# Register your models here.

@admin.register(Multa)
class MultaAdmin(admin.ModelAdmin):
    '''Admin View for Multa'''

    list_display = (
        'mul_id',
        'socio.soc_nombre',
        'mul_monto',
        'mul_estado',
        'mul_descripcion'
    )
    list_filter = ('mul_estado',)
    search_fields = (
        'socio.soc_nombre',
        'socio.soc_identificador',
    )
    ordering = ('mul_id',)