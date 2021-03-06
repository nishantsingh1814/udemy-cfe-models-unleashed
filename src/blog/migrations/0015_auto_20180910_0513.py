# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-09-10 05:13
from __future__ import unicode_literals

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20180910_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_email',
            field=models.EmailField(blank=True, max_length=240, null=True, validators=[blog.validators.validate_author_email]),
        ),
    ]
