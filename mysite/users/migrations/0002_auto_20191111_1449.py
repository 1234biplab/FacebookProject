# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-11 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
