#Author    :lwb
# -*- coding: utf-8 -*-
import random,requests,uuid
from django.core.cache import cache

from common import keys, errors
from good.models import Goods
from .models import *
from lib.httplib import render_json
from lib.sms import send_sms

def generator_token():
    token =  str(uuid.uuid4())
    return token


#发送验证码
def s_sms(request):
    phone_num = request.POST.get('phonenum')
    vcode = cache.get(keys.SMS_KEY % phone_num, None)
    if vcode:
        raise errors.Sms_Error.SMS_TIME_LIMIT
    vcode = send_sms(phone_num)
    # 把验证码放到缓存中,过期时间60秒
    cache.set(keys.SMS_KEY % phone_num, vcode, 60)
    return render_json()

# 注册/登录
def register_login(request):
    vcode = request.POST.get('vcode')
    phone_num = request.POST.get('phonenum')
    re_vcode = cache.get(keys.SMS_KEY % phone_num, None)
    if not re_vcode == int(vcode):
        raise errors.Other_Error.NOT_VERIFIER
    cache.delete(keys.SMS_KEY % phone_num)

    username = request.POST.get('username')
    # password = request.POST.get('password')

    users = User.objects.filter(phonenum=phone_num)
    if not users.exists():
        user = User.objects.create(phonenum=phone_num, name=username)#, password=password)
    else:
        user = users.first()
    request.session['uid'] = user.id
    return render_json()


#首页 GET
def home(request):
    # 取出所有的商品
    goods = Goods.objects.all()

    goods = goods.filter(cgid=0)

    return render_json(goods)


# 分类 GET
def get_goods(request):
    cart_id = request.GET.get("cartid")
    child_cid = request.GET.get("childcid")
    num = request.GET.get("num",0)
    try:
        num = int(num)
        if num < 0:
            num = 0
    except:
        num = 0
    if child_cid:
        if not num:
            goods = Goods.objects.filter(categoryid = cart_id, childcid = child_cid).
    else:
        goods = Goods.objects.filter(categoryid = cart_id)

    return render_json(goods)