# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-05 02:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0040_auto_20170405_0211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='comment',
            new_name='message',
        ),
    ]
