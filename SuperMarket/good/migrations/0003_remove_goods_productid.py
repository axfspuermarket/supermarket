# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-22 05:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0002_auto_20190422_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='productid',
        ),
    ]
