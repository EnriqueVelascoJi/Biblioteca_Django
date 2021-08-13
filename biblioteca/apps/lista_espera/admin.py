from django.contrib import admin

#Importamos el modelo
from .models import ListaEspera

# Register your models here.

@admin.register(ListaEspera)
class ListaEsperaAdmin(admin.ModelAdmin):
    '''Admin View for ListaEspera'''

    list_display = (
        'le_id',
        'socio',
        'libro',
        'le_estado',
    )
    list_filter = ('le_estado',)
    search_fields = (
        'socio.soc_nombre',
        'libro.lib_titulo',
    )
    ordering = ('le_id',)