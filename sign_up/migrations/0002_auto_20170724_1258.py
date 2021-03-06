# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-24 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='password',
            field=models.CharField(default=123, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consumer',
            name='email',
            field=models.EmailField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
