# -*- coding: utf-8 -*-
# @Author: bn
# @Date:   2018-05-28 22:57:07
# @Last Modified by:   chenbin
# @Last Modified time: 2018-06-22 11:55:10
from django import forms

class cms_loginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(min_length=6,error_messages={' min_length':'password is too short!'})
	remember = forms.BooleanField(required=False)


class cmsDeleteAuthorForm(forms.Form):
	author_uid = forms.UUIDField(required=True)

