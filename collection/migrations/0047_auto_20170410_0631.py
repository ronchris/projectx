# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-10 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0046_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
