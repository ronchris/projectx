# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-14 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0024_destination_municipality'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('coords', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='muni',
            name='province',
            field=models.ForeignKey(default='Catanduanes', on_delete=django.db.models.deletion.CASCADE, to='collection.Province'),
            preserve_default=False,
        ),
    ]
