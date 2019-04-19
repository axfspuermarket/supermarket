#Author    :MrDan
# -*- coding: utf-8 -*-
from good.models import Goods
#获取商品
def get_goods(cart_id,child_cid,num):
    try:
        num = int(num)
        if num < 1:
            num = 1
    except:
        num = 0
    if child_cid:
        if not num:
            goods = Goods.objects.filter(categoryid=cart_id, childcid=child_cid)
        else:
            goods = Goods.objects.filter(categoryid=cart_id, childcid=child_cid)[1:num + 1]
    else:
        if not num:
            goods = Goods.objects.filter(categoryid=cart_id)
        else:
            goods = Goods.objects.filter(categoryid=cart_id)[1:num + 1]
    return goods

#获取商品
def get_goods_by_cart(cart_id):
    if child_cid:
        if not num:
            goods = Goods.objects.filter(categoryid=cart_id, childcid=child_cid)
        else:
            goods = Goods.objects.filter(categoryid=cart_id, childcid=child_cid)[1:num + 1]
    else:
        if not num:
            goods = Goods.objects.filter(categoryid=cart_id)
        else:
            goods = Goods.objects.filter(categoryid=cart_id)[1:num + 1]
    return goods