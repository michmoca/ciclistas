# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-25 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciclistasapp', '0008_auto_20190425_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='anio_edicion',
            field=models.IntegerField(),
        ),
    ]
