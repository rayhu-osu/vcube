# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-01 23:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0003_consumersequence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumersequence',
            name='driver',
        ),
        migrations.DeleteModel(
            name='ConsumerSequence',
        ),
    ]
