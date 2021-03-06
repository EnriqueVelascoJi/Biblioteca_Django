# Generated by Django 3.2.6 on 2021-08-13 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('ven_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('ven_forma_pago', models.CharField(choices=[('0', 'efectivo'), ('1', 'tarjeta de débito'), ('0', 'tarjeta de crédito')], max_length=20, verbose_name='Forma de pago')),
                ('ven_fecha', models.DateTimeField(auto_now=True, verbose_name='Fecha')),
                ('ven_impuesto', models.IntegerField(default=16, verbose_name='Impuesto')),
                ('ven_total', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Total')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('dv_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('dv_cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('dv_descuento', models.IntegerField(default=0, verbose_name='Descuento')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.libro')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.venta')),
            ],
            options={
                'verbose_name': 'DetalleVenta',
                'verbose_name_plural': 'DetalleVentas',
            },
        ),
    ]
