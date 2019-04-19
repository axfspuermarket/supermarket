#Author    :LYS
# -*- coding: utf-8 -*-
from uuid import uuid4
from order.models import Order_to_Goods
from lib.verify import my_sha256
from cart.models import Cart
from .models import Order
from common import errors, keys

def sell(order_no, discount=0, credits=0, coupons=None):
    price = Order.objects.get(id=order_no).total_price


def deal_cart(user):
    carts = Cart.objects.filter(user_id=user.id)
    if not user.cart:
        raise errors.Cart_Error.NOT_THIS_CART
    order = Order()
    order.user_id = user.id
    order.order_no = my_sha256(str(uuid4()))
    order.save()

    # 把每一个商品创建一个商品订单
    for cart in carts:
        # 创建一个商品订单
        order_to_goods = Order_to_Goods()

        # 计算总价，把已选择商品计算总价
        if cart.is_select:
            order_to_goods.order_id = order.id
            order_to_goods.goods_id = cart.goods_id
            order_to_goods.price = cart.goods.price
            order_to_goods.num = cart.num
            order_to_goods.save()

    # 清空已选中结算的商品，未选中的不清除
    Cart.objects.filter(user_id=user.id, selected=True).delete()
    return order.order_no