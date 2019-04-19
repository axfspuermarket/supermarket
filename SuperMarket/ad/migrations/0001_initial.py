# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-19 03:43
from __future__ import unicode_literals

from django.db import migrations, models
import lib.orm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200, verbose_name='图片地址')),
                ('name', models.CharField(max_length=50, verbose_name='图片名')),
                ('trackid', models.CharField(max_length=50, verbose_name='追踪ID')),
            ],
            options={
                'db_table': 'axf_nav',
            },
            bases=(models.Model, lib.orm.ModelMixin),
        ),
        migrations.CreateModel(
            name='Mainshow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200, verbose_name='图片地址')),
                ('name', models.CharField(max_length=50, verbose_name='图片名')),
                ('trackid', models.CharField(max_length=50, verbose_name='追踪ID')),
                ('categoryid', models.CharField(max_length=20, verbose_name='类别ID')),
                ('brandname', models.CharField(max_length=30, verbose_name='品牌名称')),
                ('img1', models.CharField(max_length=200, verbose_name='商品图片1')),
                ('childcid1', models.CharField(max_length=20, verbose_name='子分类')),
                ('productid1', models.CharField(max_length=20, verbose_name='产品编号')),
                ('longname1', models.CharField(max_length=100, verbose_name='完整名称')),
                ('price1', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格1')),
                ('marketprice1', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='闪购价1')),
                ('img2', models.CharField(max_length=200, verbose_name='商品图片2')),
                ('childcid2', models.CharField(max_length=20, verbose_name='子分类2')),
                ('productid2', models.CharField(max_length=20, verbose_name='产品编号2')),
                ('longname2', models.CharField(max_length=100, verbose_name='完整名称2')),
                ('price2', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格2')),
                ('marketprice2', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='闪购价2')),
                ('img3', models.CharField(max_length=200, verbose_name='产品图片3')),
                ('childcid3', models.CharField(max_length=20, verbose_name='子分类3')),
                ('productid3', models.CharField(max_length=20, verbose_name='产品编号3')),
                ('longname3', models.CharField(max_length=200, verbose_name='完整名称3')),
                ('price3', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格3')),
                ('marketprice3', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='闪购价3')),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
            bases=(models.Model, lib.orm.ModelMixin),
        ),
        migrations.CreateModel(
            name='MainWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200, verbose_name='图片地址')),
                ('name', models.CharField(max_length=50, verbose_name='图片名')),
                ('trackid', models.CharField(max_length=50, verbose_name='追踪ID')),
            ],
            options={
                'db_table': 'axf_wheel',
            },
            bases=(models.Model, lib.orm.ModelMixin),
        ),
        migrations.CreateModel(
            name='Mustbuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200, verbose_name='图片地址')),
                ('name', models.CharField(max_length=50, verbose_name='图片名')),
                ('trackid', models.CharField(max_length=50, verbose_name='追踪ID')),
            ],
            options={
                'db_table': 'axf_mustbuy',
            },
            bases=(models.Model, lib.orm.ModelMixin),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200, verbose_name='图片地址')),
                ('name', models.CharField(max_length=50, verbose_name='图片名')),
                ('trackid', models.CharField(max_length=50, verbose_name='追踪ID')),
            ],
            options={
                'db_table': 'axf_shop',
            },
            bases=(models.Model, lib.orm.ModelMixin),
        ),
    ]