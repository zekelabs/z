# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataInventoryMgmt', '0004_auto_20170411_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='downloads_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
