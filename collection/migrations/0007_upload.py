# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-11 22:22
from __future__ import unicode_literals

import collection.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_destination_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=collection.models.get_image_path)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to='collection.Destination')),
            ],
        ),
    ]
