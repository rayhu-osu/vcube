# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='image',
            field=models.ImageField(default=1, upload_to='img/'),
            preserve_default=False,
        ),
    ]
