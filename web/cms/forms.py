# -*- coding: utf-8 -*-
# @Author: bn
# @Date:   2018-05-28 22:57:07
# @Last Modified by:   chenbin
# @Last Modified time: 2018-07-19 16:47:13
from django import forms
from common.forms import BaseForm
from utils.captcha.bncaptcha import Captcha

class cms_loginForm(BaseForm):
	username = forms.CharField()
	password = forms.CharField(min_length=6,error_messages={'min_length':'password is too short!'})
	remember = forms.BooleanField(required=False)
	captcha = forms.CharField(min_length=4,max_length=4,error_messages={'min_length':'请输入4位验证码'})

	def clean_captcha(self):
		captcha = self.cleaned_data.get('captcha').lower()
		if Captcha.check_captcha(captcha):
			return captcha
		else:
			raise forms.ValidationError('captcha is error!')

class cmsDeleteAuthorForm(BaseForm):
	author_uid = forms.UUIDField(required=True)

class cmsfrontAuthForm(BaseForm):
	username = forms.CharField(max_length=20)
	tel = forms.CharField(max_length=20)
	email = forms.EmailField()
	new_psw = forms.CharField(min_length=6,error_messages={'min_length':'密码至少6位！','required':'请输入新密码！'})

class cmsArticleQueryForm(BaseForm):
	title = forms.CharField(max_length=20,required=False)
	author = forms.CharField(max_length=20,required=False)
	category = forms.CharField(max_length=20,required=False)
	c_page = forms.IntegerField(min_value=1)

class cmsAddCategoryForm(BaseForm):
	name = forms.CharField(max_length=20,error_messages={'required':'请输入分类信息'})

class cmsAddTagForm(BaseForm):
	name = forms.CharField(max_length=20,error_messages={'required':'请输入标签信息'})

class cmsArticleModifyForm(BaseForm):
	title = forms.CharField(max_length=100)
	category_id = forms.IntegerField(min_value=1)
	content = forms.CharField()

class cmsTopArticleForm(BaseForm):
	uid = forms.UUIDField(required=True)

#删除文章表单验证
class cmsDeleteArticleForm(cmsTopArticleForm):
	pass