# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-22 02:15
from __future__ import unicode_literals

from django.db import migrations, models
import lib.orm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='手机')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱')),
                ('img', models.CharField(blank=True, max_length=256, null=True, verbose_name='头像')),
                ('credits', models.IntegerField(default=0, verbose_name='积分')),
            ],
            bases=(models.Model, lib.orm.ModelMixin),
        ),
        migrations.CreateModel(
            name='UserAdress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='用户ID')),
                ('name', models.CharField(max_length=30, verbose_name='收货人')),
                ('phone', models.CharField(max_length=30, verbose_name='联系方式')),
                ('adress', models.CharField(max_length=100, verbose_name='收货地址')),
            ],
            bases=(models.Model, lib.orm.ModelMixin),
        ),
    ]
