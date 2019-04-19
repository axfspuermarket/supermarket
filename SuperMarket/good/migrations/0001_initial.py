# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-19 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=20, verbose_name='产品ID')),
                ('productimg', models.CharField(max_length=200, verbose_name='产品图')),
                ('productname', models.CharField(max_length=30, verbose_name='产品名')),
                ('productlongname', models.CharField(max_length=50, verbose_name='产品长名称')),
                ('isxf', models.BooleanField(verbose_name='平台推荐')),
                ('pmdesc', models.BooleanField(verbose_name='pm降序')),
                ('specifics', models.CharField(max_length=30, verbose_name='产品规格/重量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
                ('marketprice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='市场价')),
                ('categoryid', models.IntegerField(verbose_name='分类ID')),
                ('childcid', models.IntegerField(verbose_name='子类ID')),
                ('childcidname', models.CharField(max_length=30, verbose_name='子类名')),
                ('storenums', models.IntegerField(verbose_name='库存')),
                ('productnum', models.IntegerField(verbose_name='销量')),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
        migrations.CreateModel(
            name='Goodtypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=20, verbose_name='类型ID')),
                ('typename', models.CharField(max_length=20, verbose_name='分类名称')),
                ('childtypenames', models.CharField(max_length=200, verbose_name='子类')),
                ('typesort', models.IntegerField(verbose_name='排序类型')),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
    ]
