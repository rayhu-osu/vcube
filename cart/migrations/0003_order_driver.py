# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-31 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('valet', '0001_initial'),
        ('cart', '0002_auto_20170724_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='valet.Driver'),
        ),
    ]