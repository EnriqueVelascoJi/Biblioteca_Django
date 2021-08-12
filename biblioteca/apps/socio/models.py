from django.db import models

# Create your models here.

#Modelo de tabla Socio
class Socio(models.Model):
    """Model definition for Socio."""

    reputacion = [
        ('0', 'buena'),
        ('0', 'mala')
    ]
    # TODO: Define fields here
    soc_id = models.IntegerField('Id', primary_key=True)
    soc_nombre = models.CharField('Nombre', max_length=40)
    soc_telefono = models.CharField('Télefono', max_length=15)
    soc_email = models.CharField('Email', max_length=40)
    soc_direccion = models.CharField('Dirección', max_length=50)
    soc_reputacion = models.CharField('Reptación', max_length=20, choices=reputacion)
    soc_puntos = models.IntegerField('Puntos', default=5)
    soc_identificador = models.CharField('Identificador', max_length=10)
    


    class Meta:
        """Meta definition for Socio."""

        verbose_name = 'Socio'
        verbose_name_plural = 'Socios'

    def __str__(self):
        """Unicode representation of Socio."""
        return str(self.soc_id) + '.- ' + self.soc_nombre + ' -- ' + self.soc_email + ' -- ' + self.soc_telefono

