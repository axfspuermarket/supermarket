from django.contrib import admin

# Register your models here.
from ad.models import MainWheel,MainNav,Mustbuy,Shop,Mainshow
from user.models import User,UserAdress
from good.models import Goods,Goodtypes
from event.models import Discount,CouponType,Coupon,User_to_Discount
from order.models import Order,Order_Log,Order_to_Goods
from cart.models import Cart

admin.register(MainWheel)
admin.register(MainNav)
admin.register(Mustbuy)
admin.register(Shop)
admin.register(Mainshow)
admin.register(User)
admin.register(UserAdress)
admin.register(Goods)
admin.register(Goodtypes)
admin.register(Discount)
admin.register(CouponType)
admin.register(Coupon)
admin.register(User_to_Discount)
admin.register(Order)
admin.register(Order_Log)
admin.register(Order_to_Goods)
admin.register(Cart)