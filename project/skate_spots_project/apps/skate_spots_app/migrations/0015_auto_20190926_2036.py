# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-27 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skate_spots_app', '0014_auto_20190926_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/spot_images/'),
        ),
    ]
