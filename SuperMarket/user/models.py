from django.db import models
from lib.orm import ModelMixin
# Create your models here.
class User(models.Model,ModelMixin):
    phone = models.CharField(max_length=11, verbose_name='手机', unique=True)
    name = models.CharField(max_length=20, verbose_name='用户名', unique=True)
    password = models.CharField(max_length=256, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱', null=True, blank=True)
    img = models.CharField(max_length=256, verbose_name='头像', null=True, blank=True)
    credits = models.IntegerField(default=0, verbose_name="积分")
    # token = models.CharField(max_length=256, editable=False)
    @property
    def address(self):
        if not hasattr(self, "_address"):
            self._address = UserAdress.objects.filter(uid=self.id)
            return self._address


class UserAdress(models.Model):
    uid = models.IntegerField(verbose_name='用户ID')
    name = models.CharField(max_length=30, verbose_name='收货人')
    phone = models.CharField(max_length=30, verbose_name='联系方式')
    adress = models.CharField(max_length=100, verbose_name='收货地址')

    def __str__(self):
        return self.name
