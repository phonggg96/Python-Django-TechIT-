# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20171013_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tintuc',
            name='Title',
            field=models.CharField(max_length=500, null=True),
        ),
    ]