#Author    :lwb
# -*- coding: utf-8 -*-

from django.core.cache import cache
from common import keys, errors
from .models import *
from lib.httplib import render_json
from lib.sms import send_sms


#发送验证码
def s_sms(request):
    phone_num = request.POST.get('phone')
    vcode = cache.get(keys.SMS_KEY % phone_num, None)
    if vcode:
        raise errors.Sms_Error.SMS_TIME_LIMIT
    vcode = send_sms(phone_num)
    # 把验证码放到缓存中,过期时间60秒
    cache.set(keys.SMS_KEY % phone_num, vcode, 60)
    # print(phone_num)
    return render_json()

# 注册/登录
def register_login(request):
    vcode = request.POST.get('vcode')
    phone_num = request.POST.get('phone')

    username = request.POST.get('username', phone_num)
    password = request.POST.get('password')
    re_vcode = cache.get(keys.SMS_KEY % phone_num, None)
    # print(re_vcode,vcode)
    if not str(re_vcode) == str(vcode):
        raise errors.Other_Error.NOT_VERIFIER
    cache.delete(keys.SMS_KEY % phone_num)
    users = User.objects.filter(phone=phone_num)
    if not users.exists():
        user = User.objects.create(phone=phone_num, name=username,password=password)#, password=password)
    else:
        user = users.first()
    request.session['uid'] = user.id
    return render_json()


