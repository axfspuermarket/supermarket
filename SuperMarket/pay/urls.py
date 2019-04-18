#Author    :MrDan
# -*- coding: utf-8 -*-
from django.conf.urls import url
from .api import *
urlpatterns = [
    url(r'^pay/$',pay),
    url(r'^pay/$',pay),
    url(r'^notify/$',notify),
]