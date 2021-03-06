from django.db import models
#Importamos los modelos externos
from apps.libro.models import Libro

# Create your models here.
#Modelo del prestamo
class Prestamo(models.Model):
    """Model definition for Prestamo."""

    # TODO: Define fields here
    pre_id = models.AutoField('Id', primary_key=True)
    pre_hora_prestamo = models.TimeField('Hora prestámo', auto_now=True)
    pre_hora_regreso = models.TimeField('Hora regreso')
    pre_fecha = models.DateField('Fechas', auto_now=True)

    class Meta:
        """Meta definition for Prestamo."""

        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'

    def __str__(self):
        """Unicode representation of Prestamo."""
        return "{}.- ({}) -- ({})".format(self.pre_id, self.pre_hora_prestamo, self.pre_hora_regreso)

#Modelo de la ficha de prestamo
class FichaPrestamo(models.Model):
    """Model definition for FichaPrestamo."""

    # TODO: Define fields here
    fp_id = models.AutoField('Id', primary_key=True)
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fp_estado = models.BooleanField('Estado', default=True)

    class Meta:
        """Meta definition for FichaPrestamo."""

        verbose_name = 'Ficha de Préstamo'
        verbose_name_plural = 'Fichas de Prestamo'

    def __str__(self):
        """Unicode representation of FichaPrestamo."""
        return "{}.- ({}) -- ({})".format(self.fp_id, self.libro.lib_titulo, self.fp_estado)

