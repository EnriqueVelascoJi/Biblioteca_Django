from django.db import models

#Importar modelo
from apps.socio.models import Socio
from apps.libro.models import Libro

# Create your models here.

#Modelo de Lista de Espera
class ListaEspera(models.Model):
    """Model definition for ListaEspera."""

    # TODO: Define fields here
    le_id = models.AutoField('Id', primary_key=True)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    le_estado = models.BooleanField('Estado', default=True)


    class Meta:
        """Meta definition for ListaEspera."""

        verbose_name = 'Lista de Espera'
        verbose_name_plural = 'Listas de Espera'

    def __str__(self):
        """Unicode representation of ListaEspera."""
        return "{}.- {} -- ({}) - [{}]".format(self.le_id, self.socio.soc_nombre, self.libro_lib_titulo, self.le_estado)
