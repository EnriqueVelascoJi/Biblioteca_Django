from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Libro(models.Model):
    """Model definition for Libro."""

    # TODO: Define fields here
    lib_id = models.IntegerField('Id', primary_key=True)
    lib_titulo = models.CharField('Título', max_length=50)
    lib_autor = models.CharField('Autor', max_length=50)
    lib_isbn = models.CharField('ISBN', max_length=13)
    lib_editorial = models.CharField('Editorial', max_length=15)
    lib_edicion = models.IntegerField('Edición', default=1)
    lib_copias_venta = models.IntegerField('Copias_venta', default=0)
    lib_copias_servicio = models.IntegerField('Copias_servicio', default=0)
    lib_precio = models.DecimalField('Precio', max_digits=6, decimal_places=2, default=0)

    class Meta:
        """Meta definition for Libro."""

        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        """Unicode representation of Libro."""
        return str(self.lib_id) + '.- ' + self.lib_titulo + '--' + self.lib_autor

