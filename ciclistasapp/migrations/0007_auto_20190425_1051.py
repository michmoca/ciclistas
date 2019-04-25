# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-25 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ciclistasapp', '0006_auto_20190425_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pruebasequipo',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Equipo', to='ciclistasapp.Equipo'),
        ),
    ]
