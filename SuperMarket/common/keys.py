#sms缓存
SMS_KEY = 'Vcode-%s'

#访问主机
HOST_KEY = 'Host-%s'

#订单
class Order_Status:
    #已完成
    ORDER_IS_FINISH = 0
    #未支付
    ORDER_UNPAY = 1

    #配送中
    ORDER_DISPATCHING = 2

    #已收货
    ORDER_ARRIVED = 3

    #未评论
    RECEIVE_UNCOMMENT = 4

    #售后中
    ORDER_SERVICE = 5