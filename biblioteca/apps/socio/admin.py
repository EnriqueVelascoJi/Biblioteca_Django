from django.contrib import admin

#Importamos el modelo externo
from .models import Socio

# Register your models here.

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    '''Admin View for Socio'''

    list_display = (
        'soc_id',
        'soc_nombre',
        'soc_telefono',
        'soc_email',
        'soc_direccion',
        'soc_reputacion',
        'soc_puntos',
        'soc_identificador',
    )
    list_filter = ('soc_reputacion', )
    search_fields = (
        'soc_nombre',
        'soc_email',
        'soc_identificador',
    )
    ordering = ('soc_id',)