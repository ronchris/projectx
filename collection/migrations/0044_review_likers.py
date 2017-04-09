# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-07 05:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0043_review_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='likers',
            field=models.ManyToManyField(related_name='likers', to=settings.AUTH_USER_MODEL),
        ),
    ]
