# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-09 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(upload_to='profiles/'),
        ),
    ]
