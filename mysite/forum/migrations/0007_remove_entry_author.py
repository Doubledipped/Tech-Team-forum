# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 18:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20171210_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='author',
        ),
    ]