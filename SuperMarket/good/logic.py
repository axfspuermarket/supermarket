#Author    :MrDan
# -*- coding: utf-8 -*-
from good.models import Goods
#获取商品
def get_goods(type_id,child_cid,num):
    try:
        num = int(num)
        if num < 1:
            num = 1
    except:
        num = 0
    # if child_cid:
    #     if not num:
    #         goods = Goods.objects.filter(categoryid=type_id, childcid=child_cid)
    #     else:
    #         goods = Goods.objects.filter(categoryid=type_id, childcid=child_cid)[1:num + 1]
    # else:
    if not num:
        goods = Goods.objects.filter(categoryid=type_id)
    else:
        goods = Goods.objects.filter(categoryid=type_id)[1:num + 1]
    return [good.to_dict() for good in goods]

