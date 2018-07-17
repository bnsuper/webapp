# -*- coding: utf-8 -*-
# @Author: chenbin
# @Date:   2018-07-06 16:13:14
# @Last Modified by:   chenbin
# @Last Modified time: 2018-07-06 16:23:10
from django.conf.urls import url
from front import views

urlpatterns = [
    url(r'^$', views.front_index, name='front_index'),
    url(r'^article/(?P<uid>[\w\-]+)/$', views.front_article, name='front_article'),
    url(r'^sign_in/$', views.front_sign_in, name='front_sign_in'),
    url(r'^sign_up/$', views.front_sign_up, name='front_sign_up'),
]
