# -*- coding: utf-8 -*-
# @Author: bn
# @Date:   2018-05-28 22:57:07
# @Last Modified by:   chenbin
# @Last Modified time: 2018-06-26 10:22:15
from django import forms

class cms_loginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(min_length=6,error_messages={'min_length':'password is too short!'})
	remember = forms.BooleanField(required=False)


class cmsDeleteAuthorForm(forms.Form):
	author_uid = forms.UUIDField(required=True)

class cmsfrontAuthForm(forms.Form):
	username = forms.CharField(max_length=20)
	tel = forms.CharField(max_length=20)
	email = forms.EmailField()
	new_psw = forms.CharField(min_length=6,error_messages={'min_length':'密码至少6位！','required':'请输入新密码！'})

class cmsArticleQueryForm(forms.Form):
	title = forms.CharField(max_length=20,required=False)
	author = forms.CharField(max_length=20,required=False)
	category = forms.CharField(max_length=20,required=False)
	c_page = forms.IntegerField(min_value=1)