from django.db import models


# Create your models here.
from common import errors
class EventModels(models.Model):
    name =  models.CharField(max_length=20, verbose_name="活动名")
    describe = models.CharField(max_length=100, verbose_name="活动描述")
    img = models.CharField(max_length=100, verbose_name="活动图片")
    start_date = models.DateField(verbose_name="活动开始日期")
    end_date = models.DateField(verbose_name="活动结束日期")
    def is_valid(self):
        if self.start_date.day >= self.end_date.day+1:
            raise errors.Other_Error.MODEL_ERROR
        return True

    class Meta:
        abstract = True  # 抽象类,不会生成数据库表
    def __str__(self):
        return self.name

#折扣
class Discount(EventModels):
    constraint_price = models.IntegerField(verbose_name="条件值")
    discount_rate = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="折扣率")
    class Meta:
        db_table = 'discount'


#优惠卷设计
class CouponType(EventModels):
    constraint_price = models.IntegerField(verbose_name="条件值")
    reduce_price = models.IntegerField(verbose_name="减少值")
    @property
    def coupon_residue(self):
        #优惠卷剩余
        return len(Coupon.objects.filter(coupon_type_id=self.id, coupon_status = 0))
    class Meta:
        db_table = 'coupontype'

class Coupon(EventModels):
    coupon_type_id = models.IntegerField("优惠卷类型")
    coupon_no = models.IntegerField("优惠卷编号")
    coupon_status = models.BooleanField(default=False,verbose_name="是否被使用")
    use_date = models.DateField("优惠卷使用时间",null=True)
    user_id = models.IntegerField(verbose_name="用户ID")
    @property
    def coupontype(self):
        if not hasattr(self,"_coupontype"):
            self._coupontype = CouponType.objects.get(self.coupon_type_id)
        return self._coupontype
    class Meta:
        db_table = 'coupon'

class User_to_Discount(models.Model):
    discount_type_id = models.IntegerField("折扣类型ID")
    user_id = models.IntegerField(verbose_name="用户ID")
    @property
    def discount_type(self):
        if not hasattr(self,"_discount_type"):
            self._discount_type = Discount.objects.get(self.discount_type_id)
        return self._discount_type