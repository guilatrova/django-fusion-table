# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-19 10:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('lat', 'lon')]),
        ),
    ]