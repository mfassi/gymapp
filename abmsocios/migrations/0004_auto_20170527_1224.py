# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abmsocios', '0003_auto_20170515_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=2),
        ),
        migrations.AlterModelTable(
            name='datosmedicos',
            table='abmsocios_datosmedicos',
        ),
        migrations.AlterModelTable(
            name='obrasocial',
            table='abmsocios_obrasocial',
        ),
        migrations.AlterModelTable(
            name='socio',
            table='abmsocios_socio',
        ),
        migrations.AlterModelTable(
            name='telefono',
            table='abmsocios_telefono',
        ),
    ]
