#Author    :MrDan
# -*- coding: utf-8 -*-
from order.models import Order
def sell(order_no,discount = 0, credits=0,coupons = None):
    price = Order.objects.get(id=order_no).total_price

