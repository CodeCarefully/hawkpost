# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-29 15:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('humans', '0011_keychangerecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='server_signed',
        ),
    ]
