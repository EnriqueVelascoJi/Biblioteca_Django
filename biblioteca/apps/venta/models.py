from django.db import models

#Importamos los modelos externos
from apps.libro.models import Libro

# Create your models here.
#Modelo de Venta
class Venta(models.Model):
    """Model definition for Venta."""

    formas_pago = [
        ('0', 'efectivo'),
        ('1', 'tarjeta de débito'),
        ('0', 'tarjeta de crédito'),
    ]
    # TODO: Define fields here
    ven_id = models.AutoField('Id', primary_key=True)
    ven_forma_pago = models.CharField('Forma de pago', choices=formas_pago, max_length=20)
    ven_fecha = models.DateTimeField('Fecha', auto_now=True, auto_now_add=False)
    ven_impuesto = models.IntegerField('Impuesto', default=16)
    ven_total = models.DecimalField('Total', max_digits=7, decimal_places=2)
    
    class Meta:
        """Meta definition for Venta."""

        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        """Unicode representation of Venta."""
        return "{}.- ({}) -- ({})".format(self.ven_id, self.ven_forma_pago, self.ven_total)

#Modelo de Datalle de Venta
class DetalleVenta(models.Model):
    """Model definition for DetalleVenta."""

    # TODO: Define fields here
    dv_id = models.AutoField('Id', primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    dv_cantidad = models.IntegerField('Cantidad', default=1)
    dv_descuento = models.IntegerField('Descuento', default=0)

    class Meta:
        """Meta definition for DetalleVenta."""

        verbose_name = 'DetalleVenta'
        verbose_name_plural = 'DetalleVentas'

    def __str__(self):
        """Unicode representation of DetalleVenta."""
        return str(self.dv_id) + '.- ' + self.libro.lib_titulo + '-- $' + self.dv_cantidad
