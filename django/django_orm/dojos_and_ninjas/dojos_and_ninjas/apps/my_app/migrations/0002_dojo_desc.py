# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-12 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='A description of the dojo', max_length=255),
        ),
    ]
