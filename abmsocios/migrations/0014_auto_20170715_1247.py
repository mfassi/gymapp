# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-15 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abmsocios', '0013_auto_20170712_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_medicos',
            name='socio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='abmsocios.Socio'),
        ),
    ]
