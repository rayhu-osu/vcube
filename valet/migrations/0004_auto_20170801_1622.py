# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-01 20:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valet', '0003_sequence_driver'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sequence',
            new_name='StoreSequence',
        ),
    ]
