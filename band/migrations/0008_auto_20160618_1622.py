# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0007_auto_20160618_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='listenLink',
            field=models.CharField(max_length=150),
        ),
    ]