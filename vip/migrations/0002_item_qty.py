# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Qty',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
    ]