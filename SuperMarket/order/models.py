from django.db import models
from user.models import User
from good.models import Goods


# Create your models here.
class OrderMain(models.Model):
    user = models.ForeignKey(User)
    goods = models.ForeignKey(Goods)
    num = models.IntegerField(default=1)

    class Meta:
        abstract = True  # 抽象类,不会生成数据库表


class Order(models.Model):
    statusChoice = ((0, '未付款'), (1, '配送中'), (2, '已完成'), (3, '待评价'), (4, '售后中'), (5, '已删除'))
    status = models.IntegerField(choices=statusChoice, default=0, verbose_name='订单状态')
    user_id = models.IntegerField(verbose_name='用户编号')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    order_to_goods_id = models.IntegerField('订单详情')
    order_no = models.CharField( max_length=256, verbose_name="订单号")
    @property
    def order_log(self):
        if not hasattr(self,"_order_log"):
            self._order_log = Order_Log.objects.get(order_id=self.id)
        return self._order_log
    @property
    def total_price(self):
        order_to_good_list = Order_to_Goods.objects.filter(order_id=self.id)
        price = 0
        for order_to_good in order_to_good_list:
            price += order_to_good._good.price * order_to_good.good_num
        return price

#订单日志
class Order_Log(models.Model):
    order_id = models.IntegerField(verbose_name="订单ID")
    coupon_price = models.IntegerField(verbose_name="优惠价格")
    credit_price = models.IntegerField(verbose_name="积分抵扣价格")
    discount = models.IntegerField(verbose_name="折扣价格")
    price = models.DecimalField(verbose_name="订单总价")
    def order(self):
        if not hasattr(self,"_order"):
            self._order = Order.objects.get(self.order_id)
        return self._order

class Order_to_Goods(models.Model):
    order_id = models.IntegerField(verbose_name='订单ID')
    good_id = models.IntegerField( verbose_name='商品ID')
    good_num = models.IntegerField(verbose_name='商品数量')
    @property
    def good(self):
        if not hasattr(self,"_good"):
            self._good = Goods.objects.get(id = self.good_id)
        return self._good



class Cart(OrderMain):
    is_select = models.BooleanField(default=True)
    is_del = models.BooleanField(default=0)
