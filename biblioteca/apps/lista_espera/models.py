from biblioteca.apps.libro.models import Libro
from biblioteca.apps.socio.models import Socio
from django.db import models

# Create your models here.

#Modelo de Lista de Espera
class ListaEspera(models.Model):
    """Model definition for ListaEspera."""

    # TODO: Define fields here
    le_id = models.IntegerField('Id', primary_key=True)
    socio = models.ForeignKey('Socio', Socio)
    libro = models.ForeignKey('Libro', Libro)
    le_estado = models.BooleanField('Estado', default=True)


    class Meta:
        """Meta definition for ListaEspera."""

        verbose_name = 'Lista de Espera'
        verbose_name_plural = 'Listas de Espera'

    def __str__(self):
        """Unicode representation of ListaEspera."""
        return "{}.- {} -- ({}) - [{}]".format(self.le_id, self.socio.soc_nombre, self.libro_lib_titulo, self.le_estado)
