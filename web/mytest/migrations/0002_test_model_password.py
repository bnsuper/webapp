# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-24 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_model',
            name='password',
            field=models.CharField(default=123456, max_length=20),
            preserve_default=False,
        ),
    ]
