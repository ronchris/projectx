# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-14 22:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0025_auto_20170314_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='muni',
            name='province',
        ),
    ]
