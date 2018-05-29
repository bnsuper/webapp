# -*- coding: utf-8 -*-
# @Author: bn
# @Date:   2018-05-28 22:57:07
# @Last Modified by:   bn
# @Last Modified time: 2018-05-29 00:07:50
from django import forms

class cms_loginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(min_length=6,error_messages={' min_length':'password is too short!'})
	remember = forms.BooleanField(required=False)




