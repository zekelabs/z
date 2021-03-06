# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DataInventoryMgmt', '0010_auto_20170412_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='problems')),
                ('datasets', models.ManyToManyField(to='DataInventoryMgmt.DataSet')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
