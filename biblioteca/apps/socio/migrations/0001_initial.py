# Generated by Django 3.2.6 on 2021-08-13 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('soc_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('soc_nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('soc_telefono', models.CharField(max_length=15, verbose_name='Télefono')),
                ('soc_email', models.CharField(max_length=40, verbose_name='Email')),
                ('soc_direccion', models.CharField(max_length=50, verbose_name='Dirección')),
                ('soc_reputacion', models.CharField(choices=[('0', 'buena'), ('0', 'mala')], max_length=20, verbose_name='Reptación')),
                ('soc_puntos', models.IntegerField(default=5, verbose_name='Puntos')),
                ('soc_identificador', models.CharField(max_length=10, verbose_name='Identificador')),
            ],
            options={
                'verbose_name': 'Socio',
                'verbose_name_plural': 'Socios',
            },
        ),
    ]
