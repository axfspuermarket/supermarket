from django.contrib import admin

# Register your models here.
from ad.models import MainWheel,MainNav,Mustbuy,Shop,Mainshow
from user.models import User,UserAdress
from good.models import Goods,Goodtypes
from event.models import Discount,CouponType,Coupon,User_to_Discount
from order.models import Order,Order_Log,Order_to_Goods
from cart.models import Cart

admin.site.register(MainWheel)
admin.site.register(MainNav)
admin.site.register(Mustbuy)
admin.site.register(Shop)
admin.site.register(Mainshow)
admin.site.register(User)
admin.site.register(UserAdress)
admin.site.register(Goods)
admin.site.register(Goodtypes)
admin.site.register(Discount)
admin.site.register(CouponType)
admin.site.register(Coupon)
admin.site.register(User_to_Discount)
admin.site.register(Order)
admin.site.register(Order_Log)
admin.site.register(Order_to_Goods)
admin.site.register(Cart)