# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-21 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_delete_simple'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Graph'),
        ),
    ]
