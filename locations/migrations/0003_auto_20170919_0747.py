# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-19 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20170919_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=20, max_digits=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='lon',
            field=models.DecimalField(decimal_places=20, max_digits=50),
        ),
    ]
