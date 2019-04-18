from django.db import models
from lib.orm import ModelMixin

# Create your models here.
class Main(models.Model,ModelMixin):
    img = models.CharField(max_length=200, verbose_name='图片地址')
    name = models.CharField(max_length=50, verbose_name='图片名')
    trackid = models.CharField(max_length=50, verbose_name='追踪ID')

    class Meta:
        abstract = True  # 抽象类,不会生成数据库表

    def __str__(self):
        return self.name


# 轮播图
class MainWheel(Main):
    class Meta:
        db_table = 'axf_wheel'


# 首页导航图
class MainNav(Main):
    class Meta:
        db_table = 'axf_nav'


# 必买
class Mustbuy(Main):
    class Meta:
        db_table = 'axf_mustbuy'


# 便利店
class Shop(Main):
    class Meta:
        db_table = 'axf_shop'


class Mainshow(Main):
    categoryid = models.CharField(max_length=20, verbose_name='类别ID')
    brandname = models.CharField(max_length=30, verbose_name='品牌名称')

    img1 = models.CharField(max_length=200, verbose_name='商品图片1')
    childcid1 = models.CharField(max_length=20, verbose_name='子分类')
    productid1 = models.CharField(max_length=20, verbose_name='产品编号')
    longname1 = models.CharField(max_length=100, verbose_name='完整名称')
    price1 = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格1')
    marketprice1 = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='闪购价1')

    img2 = models.CharField(max_length=200, verbose_name='商品图片2')
    childcid2 = models.CharField(max_length=20, verbose_name='子分类2')
    productid2 = models.CharField(max_length=20, verbose_name='产品编号2')
    longname2 = models.CharField(max_length=100, verbose_name='完整名称2')
    price2 = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格2')
    marketprice2 = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='闪购价2')

    img3 = models.CharField(max_length=200, verbose_name='产品图片3')
    childcid3 = models.CharField(max_length=20, verbose_name='子分类3')
    productid3 = models.CharField(max_length=20, verbose_name='产品编号3')
    longname3 = models.CharField(max_length=200, verbose_name='完整名称3')
    price3 = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格3')
    marketprice3 = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='闪购价3')

    class Meta:
        db_table = 'axf_mainshow'

    def __str__(self):
        return self.name
