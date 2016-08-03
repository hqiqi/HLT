# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-19 10:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 19, 10, 14, 8, 820000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
