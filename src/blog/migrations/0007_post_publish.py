# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-09-09 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180909_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish'), ('private', 'Private')], default='draft', max_length=120),
        ),
    ]
