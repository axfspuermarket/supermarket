#Author    :MrDan
# -*- coding: utf-8 -*-
import os
from SuperMarket import settings, config
from lib.alipay.alipay import AliPay
from SuperMarket.config import Alipay_Config
from order.models import Order, Cart
from user.models import User

from common import errors

#支付模块
def pay_logic(user,orderNo):
    my_order = Order.objects.filter(user=user, id = orderNo)
    if not my_order.exists():
        raise errors.gen_logice_error("PAY_ERROR", 4300, "订单不存在")
    alipay = ali()

    # 传递参数执行支付类里的direct_pay方法，返回签名后的支付参数，
    url = alipay.direct_pay(
        subject=User.objects.get(id=my_order[0].user_id).name + str(my_order[0].id),  # 订单名称
        # 订单号生成，一般是当前时间(精确到秒)+用户ID+随机数
        out_trade_no=my_order[0].orderid,  # 订单号
        total_amount=str(my_order[0].price),  # 支付金额
        return_url=Alipay_Config.HostIP + 'orderlist/1/'
        # return_url=config.Alipay_Config.HostIP+"notify/"  # 支付成功后，买家跳转url
    )

    # 将前面后的支付参数，拼接到支付网关
    # 注意：下面支付网关是沙箱环境，最终进行签名后组合成支付宝的url请求
    return f"https://openapi.alipaydev.com/gateway.do?{url}"


def orderpay(request):
    alipay = ali()
    if request.method == "POST":
        # 检测是否支付成功
        # 去请求体中获取所有返回的数据：状态/订单号
        from urllib.parse import parse_qs
        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)
        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]
        sign = post_dict.pop('sign', None)
        if not alipay.verify(post_dict, sign):
            raise errors.gen_logice_error("PAY_ERROR",4000,"支付失败")
        data_dic = post_dict

    else:
        params = request.GET.dict()
        sign = params.pop('sign', None)
        if not alipay.verify(params, sign):
            raise errors.gen_logice_error("PAY_ERROR", 4000, "支付失败")
        data_dic = params
    oid = data_dic.get('out_trade_no')
    if oid and data_dic.get('app_id') == Alipay_Config.AppID:
        my_order = Order.objects.filter(orderid=oid, status=0)
        if not my_order.exists():
            raise errors.gen_logice_error("ORDER_ERROR", 4000, "订单不存在")
        my_order.update(status=1)
        user = User.objects.get(id=my_order[0].user_id)
        Cart.objects.filter(user=user, is_del=True).delete()


def ali():
    alipay = AliPay(
        appid=Alipay_Config.AppID,  # 设置签约的appid
        app_notify_url=Alipay_Config.HostIP + "orderpay/",  # "http://projectsedus.com/",  # 异步支付通知服务器url
        app_private_key_path=os.path.join(settings.BASE_DIR, r"static/key/ying_yong_si_yao.txt"),  # 设置应用私钥
        alipay_public_key_path=os.path.join(settings.BASE_DIR, r"static/key/zhi_fu_bao_gong_yao.txt"),
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        debug=True,  # 默认False,            # 设置是否是沙箱环境，True是沙箱环境
        return_url=Alipay_Config.HostIP + "good/",  # "http://47.92.87.172:8000/"  # 同步买家支付通知url
    )
    return alipay