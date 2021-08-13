from django.shortcuts import render

#Impor el modelo
from .models import ListaEspera

# Create your views here.
@admin.register(ListaEspera)
class ListaEsperaAdmin(admin.ModelAdmin):
    '''Admin View for ListaEspera'''

    list_display = (
        'le_id',
        'socio.soc_nombre',
        'libro.lib_titulo',
        'le_estado'
        )
    list_filter = ('le_estado',)
    search_fields = ('le_id',
        'socio.soc_nombre',
        'libro.lib_titulo',
        'le_estado')
    ordering = ('id',)