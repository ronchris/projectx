# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-21 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0022_auto_20170321_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
