# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-14 03:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0011_auto_20170313_0554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='municipality',
        ),
        migrations.AddField(
            model_name='destination',
            name='muni',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='collection.Muni'),
            preserve_default=False,
        ),
    ]
