# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-21 02:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0021_review_star_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='star_rating',
        ),
        migrations.AddField(
            model_name='profile',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Review'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]