#Author    :LYS
# -*- coding: utf-8 -*-
import hashlib
import uuid

from SuperMarket import config
from cart.models import Cart
from common import errors, keys
from .models import Order
from order.models import Order_to_Goods
from lib.httplib import render_json

alipay = config.Alipay_Config.alipay

# 加密使用
def my_sha256(str):
    # 创建sha256对象
    m = hashlib.sha256()
    # 更新这个对象
    m.update(str.encode('utf-8'))

    return m.hexdigest()


def sell(order_no,discount = 0, credits=0,coupons = None):
    price = Order.objects.get(id=order_no).total_price

# 添加订单且加入购物车
def add_order(user):

    user_id = user.id
    # 取到当前用户购物车中所有的商品
    carts = Cart.objects.filter(user_id=user_id)
    if user.cart:
        order = Order()
        order.user_id = user_id
        order.order_no = my_sha256(str(uuid.uuid4()))
        order.save()
        total = 0
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
                total += order_to_goods.num * order_to_goods.price


        # 清空已选中结算的商品，未选中的不清除
        if total:
            carts = Cart.objects.filter(selected=True)
            carts.delete()
            order.total_price = total
            order.save()


        else:
            raise errors.Cart_Error.NOT_THIS_CART
    else:
        raise 1




# 订单
def order(request):

        # 根据订单id取出订单
        orders = Order.objects.filter(id= request.POST.get("oid"))
        if not orders:
            raise errors.Order_Error.NOT_EMPTY_ORDER
        order = orders.first()
        return render_json({'order':order})

# 订单操作
def order_handle(request):
    order_id = request.POST.get('orderid')
    orders = Order.objects.filter(user_id=request.user.id,id=order_id)
    if not orders:
        raise errors.Order_Error.NOT_THIS_ORDER
    order = orders.first()

    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order.orderid,
        total_amount=str(order.total_price),
        subject="测试订单",
        return_url="http://10.3.139.178:8000/app/result/",
        notify_url=None  # 可选, 不填则使用默认notify url
    )
    # 将前面后的支付参数，拼接到支付网关
    # 注意：下面支付网关是沙箱环境，
    re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=order_string)

    return render_json({'re_url':re_url})


# 异步支付通知url (上线后使用)
# def notify(request):
#     # print("notify:", dict(request.GET))
#     app_id = request.GET.get('app_id')
#     print(app_id)
#     return HttpResponse("支付成功:%s" % (dict(request.GET)))

# 付款成功后跳转的url
def result(request):
    # print("result:", dict(request.GET))
    data = request.GET.dict()
    # print(data)
    signature = data.pop("sign")
    # print(signature)
    success = alipay.verify(data, signature)
    if not success:
        raise errors.Pay_Error.PAY_DEFEATED
    order_id = request.GET.get("out_trade_no")
    orders = Order.objects.filter(orderid=order_id)
    orders.update(status= 0 )

    return render_json(f"支付成功:{dict(request.GET)}" )

# 更改状态 POST
def change_status(request):
    order_id = request.POST.get('orderid')
    status = request.POST.get('status')
    # 查找当前用户的订单
    orders = Order.objects.filter(user_id=request.user.id,id=order_id)
    if not orders:
        raise errors.Order_Error.NOT_THIS_ORDER
    # 更新订单状态
    orders.update(status=status)
    return render_json()

# 待收货
def order_unreceive(request):
    orders = Order.objects.filter(user_id=request.user.id, status=keys.Order_Status.RECEIVE_UNCOMMENT)
    return render_json()


# 待评价
def order_comment(request):
    orders = Order.objects.filter(user_id=request.user.id, status= keys.Order_Status.RECEIVE_UNCOMMENT)
    return render_json()

# 待付款
def order_pay(request):
    orders = Order.objects.filter(user_id=request.user.id, status=keys.Order_Status.ORDER_ARRIVED)
    return render_json()

# 售后/评价
def order_service(request):
    # 判断用户是否登录
    orders = Order.objects.filter(user_id=request.user.id, status=keys.Order_Status.ORDER_IS_FINISH)
    return render_json()


# 我的订单
def all_order(request):
    # 判断用户是否登录
    user_id = request.user.id
    order_id = request.POST.get('orderid')
    orders = Order.objects.filter(user_id=user_id)
    return render_json(orders)


# 成功支付页面（调试）
def success_pay(request):
    return render_json({"page":'success_pay/success_pay.html'})