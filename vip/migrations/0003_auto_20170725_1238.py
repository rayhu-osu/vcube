# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 12:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0002_item_qty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Qty',
            new_name='qty',
        ),
    ]