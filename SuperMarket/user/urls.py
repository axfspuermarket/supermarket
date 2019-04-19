#Author    :MrDan
# -*- coding: utf-8 -*-
from django.conf.urls import url
from .api import *
urlpatterns = [
    url(r'^api/sms/',s_sms),
    url(r'^api/login/',register_login),
    url(r'^api/address/', address)

]