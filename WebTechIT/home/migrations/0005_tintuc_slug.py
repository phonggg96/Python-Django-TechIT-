# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170925_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='tintuc',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]