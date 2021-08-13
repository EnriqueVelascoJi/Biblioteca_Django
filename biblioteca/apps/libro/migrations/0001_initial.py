# Generated by Django 3.2.6 on 2021-08-13 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('lib_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('lib_titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('lib_autor', models.CharField(max_length=50, verbose_name='Autor')),
                ('lib_isbn', models.CharField(max_length=13, verbose_name='ISBN')),
                ('lib_editorial', models.CharField(max_length=15, verbose_name='Editorial')),
                ('lib_edicion', models.IntegerField(default=1, verbose_name='Edición')),
                ('lib_copias_venta', models.IntegerField(default=0, verbose_name='Copias_venta')),
                ('lib_copias_servicio', models.IntegerField(default=0, verbose_name='Copias_servicio')),
                ('lib_precio', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Precio')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
    ]
