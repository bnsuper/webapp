# -*- coding: utf-8 -*-
# @Author: chenbin
# @Date:   2018-07-19 14:24:43
# @Last Modified by:   chenbin
# @Last Modified time: 2018-07-19 14:32:11
from django.conf.urls import url
from common import views

urlpatterns = [
    url(r'^captcha/$', views.common_captcha, name='common_captcha'),

]
