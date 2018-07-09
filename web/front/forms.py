# -*- coding: utf-8 -*-
# @Author: chenbin
# @Date:   2018-07-09 11:29:45
# @Last Modified by:   chenbin
# @Last Modified time: 2018-07-09 11:32:09
from django import forms
from common.forms import BaseForm

#前台首页点击加载更多表单验证
class FrontPageForm(BaseForm):
	c_page = forms.IntegerField(min_value=2)