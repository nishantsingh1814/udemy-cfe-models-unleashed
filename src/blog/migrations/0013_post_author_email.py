# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-09-10 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180910_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_email',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
    ]
