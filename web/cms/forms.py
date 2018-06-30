# -*- coding: utf-8 -*-
# @Author: bn
# @Date:   2018-05-28 22:57:07
# @Last Modified by:   chenbin
# @Last Modified time: 2018-06-30 12:18:21
from django import forms
from common.forms import BaseForm

class cms_loginForm(BaseForm):
	username = forms.CharField()
	password = forms.CharField(min_length=6,error_messages={'min_length':'password is too short!'})
	remember = forms.BooleanField(required=False)


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

class cmsModefyArticleForm(BaseForm):
	category = forms.IntegerField(min_value=1)

