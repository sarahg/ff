# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecasts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast',
            name='label',
            field=models.CharField(default='', max_length=200),
        ),
    ]