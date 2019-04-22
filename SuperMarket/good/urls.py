#Author    :MrDan
# -*- coding: utf-8 -*-
from django.conf.urls import url
from .api import *

urlpatterns=[
    url(r'^api/goods/',goods),
    url(r"^api/types/",types)

]
