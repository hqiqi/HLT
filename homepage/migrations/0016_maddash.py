# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-03 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0015_auto_20160321_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='MADdash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USD', models.CharField(max_length=60, verbose_name='USD')),
                ('M1', models.CharField(max_length=60, verbose_name='M1')),
                ('M5', models.CharField(max_length=60, verbose_name='M5')),
                ('M15', models.CharField(max_length=60, verbose_name='M15')),
                ('M30', models.CharField(max_length=60, verbose_name='M30')),
                ('H1', models.CharField(max_length=60, verbose_name='H1')),
            ],
        ),
    ]
