# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-09-10 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180910_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
