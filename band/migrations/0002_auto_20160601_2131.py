# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 21:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='title',
            new_name='name',
        ),
    ]
