# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-09 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0007_auto_20200210_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(upload_to='profiles/')),
                ('bio', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
