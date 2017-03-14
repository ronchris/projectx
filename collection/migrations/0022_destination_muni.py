# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-14 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0021_remove_destination_muni'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='muni',
            field=models.ForeignKey(default='virac', on_delete=django.db.models.deletion.CASCADE, to='collection.Muni'),
            preserve_default=False,
        ),
    ]
