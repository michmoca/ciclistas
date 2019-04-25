# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-25 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciclistasapp', '0005_auto_20190425_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='nombre_prueba',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='pruebasequipo',
            unique_together=set([('equipo', 'prueba')]),
        ),
    ]