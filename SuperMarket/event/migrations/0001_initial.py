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
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='活动名')),
                ('describe', models.CharField(max_length=100, verbose_name='活动描述')),
                ('img', models.CharField(max_length=100, verbose_name='活动图片')),
                ('start_date', models.DateField(verbose_name='活动开始日期')),
                ('end_date', models.DateField(verbose_name='活动结束日期')),
                ('coupon_type_id', models.IntegerField(verbose_name='优惠卷类型')),
                ('coupon_no', models.IntegerField(verbose_name='优惠卷编号')),
                ('coupon_status', models.BooleanField(default=False, verbose_name='是否被使用')),
                ('use_date', models.DateField(null=True, verbose_name='优惠卷使用时间')),
                ('user_id', models.IntegerField(verbose_name='用户ID')),
            ],
            options={
                'db_table': 'coupon',
            },
        ),
        migrations.CreateModel(
            name='CouponType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='活动名')),
                ('describe', models.CharField(max_length=100, verbose_name='活动描述')),
                ('img', models.CharField(max_length=100, verbose_name='活动图片')),
                ('start_date', models.DateField(verbose_name='活动开始日期')),
                ('end_date', models.DateField(verbose_name='活动结束日期')),
                ('constraint_price', models.IntegerField(verbose_name='条件值')),
                ('reduce_price', models.IntegerField(verbose_name='减少值')),
            ],
            options={
                'db_table': 'coupontype',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='活动名')),
                ('describe', models.CharField(max_length=100, verbose_name='活动描述')),
                ('img', models.CharField(max_length=100, verbose_name='活动图片')),
                ('start_date', models.DateField(verbose_name='活动开始日期')),
                ('end_date', models.DateField(verbose_name='活动结束日期')),
                ('constraint_price', models.IntegerField(verbose_name='条件值')),
                ('discount_rate', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='折扣率')),
            ],
            options={
                'db_table': 'discount',
            },
        ),
        migrations.CreateModel(
            name='User_to_Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_type_id', models.IntegerField(verbose_name='折扣类型ID')),
                ('user_id', models.IntegerField(verbose_name='用户ID')),
            ],
        ),
    ]
