# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0014_survivingpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='LectureSlidesPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=64)),
                ('body', models.TextField()),
            ],
        ),
    ]
