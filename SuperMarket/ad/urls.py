#Author    :MrDan
# -*- coding: utf-8 -*-
from django.conf.urls import url
from .api import home
urlpatterns = [
    url(r'^pic/',home),
]