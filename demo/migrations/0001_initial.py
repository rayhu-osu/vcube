# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('number_1', models.FloatField()),
                ('number_2', models.FloatField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]