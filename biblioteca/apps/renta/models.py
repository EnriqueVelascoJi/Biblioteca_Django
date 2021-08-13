
from django.db import models

#Imporar modelos externos
from apps.socio.models import Socio
from apps.libro.models import Libro
# Create your models here.

#Modelo de Renta
class Renta(models.Model):
    """Model definition for Renta."""

    # TODO: Define fields here
    ren_id = models.AutoField('Id', primary_key=True)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    ren_fecha_renta = models.DateField('Fecha de renta', auto_now=True)
    ren_fecha_regreso = models.DateField('Fecha de regreso', )

    class Meta:
        """Meta definition for Renta."""

        verbose_name = 'Renta'
        verbose_name_plural = 'Rentas'

    def __str__(self):
        """Unicode representation of Renta."""
        return "{}.- ({}) -- [{}]-[{}]".format(self.ren_id, self.socio.soc_nombre, self.ren_fecha_renta, self.ren_fecha_regreso)

#Modelo de Ficha de Renta
class FichaRenta(models.Model):
    """Model definition for FichaRenta."""

    # TODO: Define fields here
    fr_id = models.AutoField('Id', primary_key=True)
    renta = models.ForeignKey(Renta, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fr_estado = models.BooleanField('Estado', default=True)

    class Meta:
        """Meta definition for FichaRenta."""

        verbose_name = 'Ficha de Renta'
        verbose_name_plural = 'Fichas de Renta'

    def __str__(self):
        """Unicode representation of FichaRenta."""
        return "{}.- ({}) -- ({})".format(self.fr_id, self.libro.lib_titulo, self.fr_estado)

