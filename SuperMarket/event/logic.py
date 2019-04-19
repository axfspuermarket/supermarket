#Author    :MrDan
# -*- coding: utf-8 -*-
import datetime

from SuperMarket import config
from common import errors
from .models import Coupon,CouponType,Discount
#优惠券
def make_coupon(coupon_type_id, num = 100):
    #获取优惠券类型
    coupon_type = CouponType.objects.filter(coupon_type_id)
    if not coupon_type.exists():
        raise errors.Event_Error.NOT_THIS_EVENT
    coupon_type = coupon_type.first()
        #如果优惠券有效
    if not coupon_type.is_valid:
        raise errors.Event_Error.EVENT_NOT_VALID
    #生成num个优惠券
    for i in range(num):
        Coupon.objects.create(coupon_type_id = coupon_type.id,)

#使用积分
def use_credit(price,credits = None):
    credit = credits // config.CREDITS_EXPEND
    total_price = price - credit
    return total_price

#使用折扣
def use_discount_price(price,discount_id):
    try:
        # 获取折扣
        discount = Discount.objects.get(discount_id)
        # 判断是否符合折扣价格条件
        total_price = round(price * discount.discount_rate / 10, 2)
    except Exception as e:
        print(e)
        raise errors.Event_Error.NOT_THIS_EVENT
    return total_price

#使用优惠
def use_coupon(price,coupon_id):
    try:
        coupon = Coupon.objects.get(coupon_id)
        # 验证优惠券是否有效
        if not coupon.is_valid():
            raise errors.Event_Error.EVENT_NOT_VALID
        # 满减价格
        reduce_price = int(coupon.coupontype.reduce_price)
        # 满减条件
        constraint_price = int(coupon.coupontype.constraint_price)
        # 如果不符合满减条件,报错
        if price < constraint_price:
            raise errors.Event_Error.NOT_THIS_EVENT
        # 重新计算价格
        total_price = price - reduce_price
        coupon.coupon_status = 1
        coupon.use_date = datetime.datetime.now()
        coupon.save()
        # 总价小于0,则返回0
    except Exception as e:
        print(e)
        raise errors.Event_Error.NOT_THIS_EVENT
    return total_price if total_price > 0 else 0

