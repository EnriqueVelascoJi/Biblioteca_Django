from django.db import models

#Importamos los modelos
from apps.socio.models import Socio

# Create your models here.

#Modelo de Multa
class Multa(models.Model):
    """Model definition for Multa."""

    # TODO: Define fields here

    mul_id = models.AutoField('Id', primary_key=True)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    mul_monto = models.DecimalField('Monto de multa', max_digits=6, decimal_places=2)
    mul_descripcion = models.CharField('Descripción', max_length=50)
    mul_estado = models.BooleanField('Estado de la multa', default=True)


    class Meta:
        """Meta definition for Multa."""

        verbose_name = 'Multa'
        verbose_name_plural = 'Multas'

    def __str__(self):
        """Unicode representation of Multa."""
        return "{}.- $({}) -- ({})".format(self.mul_id, self.mul_monto, self.mul_estado)
