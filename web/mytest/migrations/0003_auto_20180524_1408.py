# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-24 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytest', '0002_test_model_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_model',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
